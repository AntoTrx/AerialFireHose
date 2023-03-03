#!/usr/bin/env python3
from audioop import add
import rospy
from qrotor_gazebo_plugin.msg import Command
from geometry_msgs.msg import Vector3, TwistStamped
from nav_msgs.msg import Odometry
import numpy as np
from .controller import PIDController
import air3d_planner.catenary_utils as cat

class QuadROSManager(object):
    """
    common class to subscribe and publish relevant topics
    """
    def __init__(self, name):
        self._name = name
        self._pos =  np.zeros(3)
        self._vel = np.zeros(3)
        self.cmd_publisher_ = rospy.Publisher("/"+name+"/command", Command, queue_size=10)
        self.twist_publisher_ = rospy.Publisher("/"+name+"/thrust_vector",TwistStamped, queue_size=10)
        odom_topic_name = "/"+name+"/"+name+"/qrotor_plugin/odometry"
        rospy.logwarn("Subscribing to "+odom_topic_name)
        self.odom_subscriber_ = rospy.Subscriber(odom_topic_name, Odometry, self.odom_callback)

        self._pidcontroller = PIDController(mass=0.9)
        self._cbfcontroller = CBF_QP()
        
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
        msg.header.stamp = rospy.Time()
        msg.twist.linear.x = thrust[0]
        msg.twist.linear.x = thrust[1]
        msg.twist.linear.x = thrust[2]
        self.twist_publisher_.publish(msg)
      
    def run(self, setpoint, additional_force=np.zeros(3)):
      # print(self._name, " ", setpoint)
      thrust = self._controller.run(self.pos, self.vel, setpoint)
      print(thrust)
      self.send_cmd_as_plugin_command(thrust)
      self.send_cmd_as_geometry_twist(thrust)


class Air3DManager(object):
  """"
  Total system manager
  TODO find a cool name
  """
  def __init__(self, ename='droneEndEffector', iname='droneIntermediate'):
      self.ename = ename
      self.e_quad = QuadROSManager(self.ename)
      self.iname = iname
      self.i_quad = QuadROSManager(self.iname)

      self.setpoint_subscriber = rospy.Subscriber("/droneEndEffector/setpoint", Odometry, self.setpoint_callback)

      self._cable_length = 4.0 # meters 4
      self._unit_cable_mass = 0.2475 # kg/meter 0.1
      self._l1 = 2.5 # fixed point <--> intermediate drone cable length 2.5
      self._l2 = 1.5 # intermediate <--> end effector cable length 1.5
      self._fraction = self._l1/(self._l1+self._l2)
      #0,-1,0.3
      self._e2i_pos_offset = np.array([0., -1., 0.1]) # Offset of intermediate quad w.r.t. end effector quad
      self._i_quad_pos_offset = np.array([0., 0., 1.0]) # Offset of end effector quad from the 3D print trajectory

      # TODO streamline this better; add state-machine setup to plan 
      # different planning modes; printing; going to a desired position
      self._setpoint = np.array([3, 0., 1.]) # end-effector desired position 

  def setpoint_callback(self, data):
      self._setpoint = np.array([data.pose.pose.position.x, data.pose.pose.position.y, 1 + data.pose.pose.position.z])
      print(self._setpoint)

  @property
  def L(self):
      return self._cable_length

  @property
  def rho(self):
      return self._unit_cable_mass


  def run(self):
      # TODO 
      # computing a naive setpoint for the intermediate drone for now
      e_sp = self._setpoint + self._i_quad_pos_offset
      i_sp = np.array([self._e2i_pos_offset[0] + e_sp[0], self._e2i_pos_offset[1] + e_sp[1], self._e2i_pos_offset[2] + e_sp[2]])

      catenary_tensions = cat.compute_tensions_in_3d(i_sp, e_sp, self._l2, self._unit_cable_mass)

      ff_int = np.zeros(3)
      ff_ee = np.zeros(3)

      ff_int = catenary_tensions[0] + np.array([0., 0., 9.81*i_sp[2]*self._unit_cable_mass]) # feedforward intermediate drone
      ff_ee = catenary_tensions[1] # feedforward end-effector drone

      self.i_quad.run(i_sp, additional_force=ff_int)
      self.e_quad.run(e_sp, additional_force=ff_ee)
