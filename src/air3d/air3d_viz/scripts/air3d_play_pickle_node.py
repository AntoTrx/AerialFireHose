#!/usr/bin/env python
import sys, os
import pickle

import rospy
import air3d_viz as av
import numpy as np
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Vector3

def publish_pickled_trajectory():
    # if len(sys.argv) < 2:
    #     sys.exit('Must provide pickle filename')
    # fname = sys.argv[1]

    # if not os.path.isfile(fname):
    #     sys.exit('pickle file does not exist')

    ### Load pickle file
    fname = '/home/kotaru/Downloads/Cube_1m_trajectory_50Hz.pickle'
    with open(fname, "rb") as pkl_handle:
        trajectory = pickle.load(pkl_handle)

    pub = rospy.Publisher("/droneEndEffector/setpoint", Odometry, queue_size=10)

    rospy.init_node('position', anonymous=True)
    rospy.loginfo("Initialzing publish trajectory rosnode")
    rate = rospy.Rate(10)  # 100hz
    traj_t = trajectory['t']
    traj_pos = trajectory['pos']
    # traj_vel = trajectory['vel']
    for i in range(len(traj_t)):
        msg = Odometry()
        position = Vector3()
        position.x = traj_pos[i,0]
        position.y = traj_pos[i,1]
        position.z = traj_pos[i,2]
        msg.pose.pose.position = position
        pub.publish(msg)

        if rospy.is_shutdown():
            break
        rate.sleep()


if __name__ == '__main__':
    try:
        publish_pickled_trajectory()
    except rospy.ROSInterruptException:
        pass
