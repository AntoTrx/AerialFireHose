#!/usr/bin/env python
import rospy
from qrotor_gazebo_plugin.msg import Command
from geometry_msgs.msg import Vector3
from nav_msgs.msg import Odometry
import numpy as np

from air3d_planner import Air3DManager

def main():
    rospy.init_node('command', anonymous=True)
    rospy.loginfo("Initialzing \"air3d_planning_node\"")
    sys = Air3DManager()
    rate = rospy.Rate(100)  # 10hz
    while not rospy.is_shutdown():
        sys.run()
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
