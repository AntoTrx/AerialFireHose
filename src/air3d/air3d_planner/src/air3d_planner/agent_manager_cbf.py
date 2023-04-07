#!/usr/bin/env python
from this import d
import rospy
from qrotor_gazebo_plugin.msg import Command
from geometry_msgs.msg import Vector3, TwistStamped
from nav_msgs.msg import Odometry
import numpy as np
import cvxpy as cvx
import casadi as ca
from .controllers import CBF_QP_OSQP
from .controllers import CBF_QP_Casadi
from .controllers import PIDController
import air3d_planner.catenary_utils as cat


from dynamic_reconfigure.server import Server
from air3d_planner.cfg import MissionControlConfig
from air3d_planner.msg import BoolStamped, ParamsStamped

class QuadROSManagerE(object):
    """ 
    common class to subscribe and publish relevant topics
    """
    def __init__(self, name):
        self._name = name
        self._pos =  np.zeros(3)
        self._vel = np.zeros(3)
        self.thrust = np.zeros(3)
        self.cmd_publisher_ = rospy.Publisher("/"+name+"/command", Command, queue_size=10)
        self.twist_publisher_ = rospy.Publisher("/"+name+"/thrust_vector",TwistStamped, queue_size=10)
        odom_topic_name = "/"+name+"/"+name+"/qrotor_plugin/odometry"
        rospy.logwarn("Subscribing to "+odom_topic_name)
        self.odom_subscriber_ = rospy.Subscriber(odom_topic_name, Odometry, self.odom_callback)
        self._controller = CBF_QP_OSQP()
        self._controller2 = PIDController()
   
    def odom_callback(self, data):
        self._pos = np.array([data.pose.pose.position.x, data.pose.pose.position.y, data.pose.pose.position.z])  
        self._vel = np.array([data.twist.twist.linear.x, data.twist.twist.linear.y, data.twist.twist.linear.z])

    @property
    def pos(self):
        return self._pos
    @pos.setter
    def pos(self, p):
        self._pos = p
    @property
    def vel(self):
        return self._vel
    @vel.setter
    def vel(self, v):
        self._vel = v
    @property
    def state(self):
        return np.concatenate((self._pos, self._vel))
    @state.setter
    def state(self, x):
        self._pos =  x[0:3]
        self._vel = x[3:6]

    def send_cmd_as_plugin_command(self, thrust):
        """send thrust value with zero yaw""" 
        msg = Command()
        msg.mode = Command.MODE_THRUST_YAW
        t = Vector3()
        t.x, t.y, t.z = thrust[0],  thrust[1],  thrust[2]
        msg.command.append(t)
        msg.yaw.append(0)
        self.cmd_publisher_.publish(msg)

    def send_cmd_as_geometry_twist(self, thrust):
        """send thrust value without any  yaw""" 
        msg = TwistStamped()
        msg.header.stamp = rospy.Time.now()
        msg.twist.linear.x = thrust[0]
        msg.twist.linear.y = thrust[1]
        msg.twist.linear.z = thrust[2]
        self.twist_publisher_.publish(msg)
      
    def run(self, setpoint, xj, vj, aj, vd=np.zeros(3), ad=np.zeros(3), cat_forces=np.zeros(3)):
      self.thrust = self._controller.run(self.pos, self.vel, setpoint, xj, vj, aj, vd=vd, ad=ad, ff=cat_forces)
      
      self.send_cmd_as_plugin_command(self.thrust)
      self.send_cmd_as_geometry_twist(self.thrust)
      
class QuadROSManagerI(object):
    """ 
    common class to subscribe and publish relevant topics
    """
    def __init__(self, name):
        self._name = name
        self._pos =  np.zeros(3)
        self._vel = np.zeros(3)
        self.thrust = np.zeros(3)
        self.cmd_publisher_ = rospy.Publisher("/"+name+"/command", Command, queue_size=10)
        self.twist_publisher_ = rospy.Publisher("/"+name+"/thrust_vector",TwistStamped, queue_size=10)
        odom_topic_name = "/"+name+"/"+name+"/qrotor_plugin/odometry"
        rospy.logwarn("Subscribing to "+odom_topic_name)
        self.odom_subscriber_ = rospy.Subscriber(odom_topic_name, Odometry, self.odom_callback)
        self._controllerPID = PIDController()
 
    def odom_callback(self, data):
        self._pos = np.array([data.pose.pose.position.x, data.pose.pose.position.y, data.pose.pose.position.z])  
        self._vel = np.array([data.twist.twist.linear.x, data.twist.twist.linear.y, data.twist.twist.linear.z])

    @property
    def pos(self):
        return self._pos
    @pos.setter
    def pos(self, p):
        self._pos = p
    @property
    def vel(self):
        return self._vel
    @vel.setter
    def vel(self, v):
        self._vel = v
    @property
    def state(self):
        return np.concatenate((self._pos, self._vel))
    @state.setter
    def state(self, x):
        self._pos =  x[0:3]
        self._vel = x[3:6]

    def send_cmd_as_plugin_command(self, thrust):
        """send thrust value with zero yaw""" 
        msg = Command()
        msg.mode = Command.MODE_THRUST_YAW
        t = Vector3()
        t.x, t.y, t.z = thrust[0],  thrust[1],  thrust[2]
        msg.command.append(t)
        msg.yaw.append(0)
        self.cmd_publisher_.publish(msg)

    def send_cmd_as_geometry_twist(self, thrust):
        """send thrust value without any  yaw""" 
        msg = TwistStamped()
        msg.header.stamp = rospy.Time.now()
        msg.twist.linear.x = thrust[0]
        msg.twist.linear.y = thrust[1]
        msg.twist.linear.z = thrust[2]
        self.twist_publisher_.publish(msg)
      
    def run(self, setpoint, vd=np.zeros(3), ad=np.zeros(3), cat_forces=np.zeros(3)):
      # print(self._name, " ", setpoint)
      self.thrust = self._controllerPID.run(self.pos, self.vel, setpoint, vd=vd, ad=ad, ff=cat_forces)
      self.send_cmd_as_plugin_command(self.thrust)
      self.send_cmd_as_geometry_twist(self.thrust)

class Air3DManager_cbf(object):
  """
  Total system manager
  TODO find a cool name
  """
  def __init__(self, ename='droneEndEffector', iname='droneIntermediate'):
      self.ename = ename
      self.e_quad = QuadROSManagerE(self.ename)

      self.iname = iname
      self.i_quad = QuadROSManagerI(self.iname)
      
      self.setpoint_subscriber = rospy.Subscriber("/droneEndEffector/setpoint", Odometry, self.setpoint_callback)
      self._mission_ctrl = Server(MissionControlConfig, self.mission_ctrl_cb, namespace="mission_control")
      self._flag_pub = rospy.Publisher("/mission_control/flag", BoolStamped, queue_size=10)
      self._params_pub = rospy.Publisher("/mission_control/params", ParamsStamped, queue_size=10)

      self._cable_length = 7 # meters
      self._unit_cable_mass = 0.1 # kg/meter
      self._l1 = 5.5 # fixed point <--> intermediate drone cable length
      self._l2 = 1.5 # intermediate <--> end effector cable length
      self._fraction = self._l1/(self._l1+self._l2)
      self._e2i_pos_offset = np.array([0., 0., 0.]) # Offset of intermediate quad w.r.t. end effector quad
      self._i_quad_pos_offset = np.array([0., 0., 1.]) # Offset of end effector quad from the 3D print trajectory

      self.use_catenary = True
      self.do_task = False
      self._task_start_time = rospy.get_time()
      self._start_lsweep = False
      self._start_lsweep_time = False
      
      # TODO streamline this better; add state-machine setup to plan 
      # different planning modes; printing; going to a desired position
      self._setpoint = np.array([6.0, 0., 1.]) # end-effector desired position 

  def setpoint_callback(self, data):
      self._setpoint = np.array([1+data.pose.pose.position.x, data.pose.pose.position.y, 1+ data.pose.pose.position.z])
      print(self._setpoint)

  def mission_ctrl_cb(self, config, level):
    rospy.loginfo("""Reconfigure Request: {radius}, {delta_radius},\ 
          {height}, {delta_height}, {angle}, {delta_angle}, {K1}, {K2}""".format(**config))
    
    self.e_r = config.radius
    self.e_dr = config.delta_radius
    self.e_h = config.height
    self.e_dh = config.delta_height
    self.e_th = config.angle*np.pi/180.
    self.e_dth = config.delta_angle*np.pi/180.
    self._K1 = config.K1
    self._K2 = config.K2
    self.use_catenary = config.USE_CATENARY
    self.do_task = config.do_task
    return config


  @property
  def L(self):
      return self._cable_length

  @property
  def rho(self):
      return self._unit_cable_mass

  def compute_trajectory(self):
      # computing a naive setpoint for the intermediate drone for now
      def getTime():
          return rospy.get_time() - self._task_start_time

      h = 1
      l = 0.5
      r = 0

      dh = 0.25/20.
      dl = 0.5/20.

      t0 = 1.75/dh

      get_h = lambda t: h + dh*t
      get_l = lambda t: l + dl*(t-t0)*(t>t0)

      l = np.maximum(0.5, np.minimum(1.45, get_l(getTime())))
      h = np.maximum(1, np.minimum(2.75, get_h(getTime())))

      e_sp = np.array([r*np.cos(self.e_th)+l*np.cos(self.e_th+self.e_dth), r*np.sin(self.e_th)+l*np.sin(self.e_th+self.e_dth), h])
      i_sp = np.array([r*np.cos(self.e_th), r*np.sin(self.e_th), h])
      self._controller = CBF_QP_OSQP()
      self._K1 = self._controller.compute_barrier_constraints.k1
      self._K2 = self._controller.compute_barrier_constraints.k2
      msg = ParamsStamped()
      msg.header.stamp = rospy.Time()
      msg.height = h
      msg.inner_radius = r
      msg.width = l
      self._params_pub.publish(msg)

      # print(e_sp, "    \t",i_sp)
      return e_sp, i_sp

  def run(self):
      
      # computing a naive setpoint for the intermediate drone for now
      ir = np.maximum(0, np.minimum(self.e_r-self.e_dr, self.e_r))
      e_sp = np.array([ir*np.cos(self.e_th) + self.e_dr*np.cos(self.e_th+self.e_dth) , ir*np.sin(self.e_th) + self.e_dr*np.sin(self.e_th+self.e_dth), self.e_h])
      i_sp = np.array([ir*np.cos(self.e_th), ir*np.sin(self.e_th), self.e_h+self.e_dh])
      
      self._controller = CBF_QP_OSQP()
      self._K1 = self._controller.k1
      self._K2 = self._controller.k2
      if self.do_task:
          e_sp, i_sp = self.compute_trajectory()

      ff_int = np.zeros(3)
      ff_ee = np.zeros(3)
      if self.use_catenary:
          try:
              rospy.logwarn("Using catenary")
              catenary_tensions = cat.compute_tensions_in_3d(i_sp, e_sp, self._l2, self._unit_cable_mass)
              ff_int = catenary_tensions[0] + np.array([0., 0., -9.81*i_sp[2]*self._unit_cable_mass]) # feedforward intermediate drone
              ff_ee = catenary_tensions[1] # feedforward end-effector drone
          except:
              rospy.logerr("Catenary computation failed")
              pass
                
      self.i_quad.run(i_sp, cat_forces=ff_int)
      self.e_quad.run(e_sp, self.i_quad._pos, self.i_quad._vel, self.i_quad.thrust, cat_forces=ff_ee)

      msg = BoolStamped()
      msg.header.stamp = rospy.Time.now()
      msg.data = self.do_task
      self._flag_pub.publish(msg)
      return
