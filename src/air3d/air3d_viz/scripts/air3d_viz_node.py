#!/usr/bin/env python
import rospy
import air3d_viz as av
import numpy as np
from nav_msgs.msg import Odometry
    
def main():
    rospy.init_node('air3d_visualizer_node', anonymous=True)
    rospy.loginfo("Initialized air3d_visualizer node!!!")

    viz_ = av.visualizer.Air3DViz()

    def callback(data):
        # rospy.loginfo(rospy.get_caller_id() + "position of end effector %f, %f, %f", data.pose.pose.position.x,data.pose.pose.position.y,data.pose.pose.position.z)
        viz_.update_pos(np.array([data.pose.pose.position.x,data.pose.pose.position.y,data.pose.pose.position.z]))

    rospy.Subscriber("/droneEndEffector/droneEndEffector/qrotor_plugin/odometry", Odometry, callback)


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    main()