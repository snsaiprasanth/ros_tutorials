#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose  # Import the Pose message type

def pose_callback(msg):
   x = msg.x
   y = msg.y
   theta = msg.theta
   print("Turtle Pose:")
   print("Position: ({}, {})".format(x, y))
   print("Orientation: {}".format(theta))

        
def turtle_pose_subscriber():
    # Initialize the ROS node
    rospy.init_node('turtle_pose_subscriber', anonymous=True)

    # Subscribe to the turtle pose topic
    rospy.Subscriber("/turtle1/pose", Pose, pose_callback)

    # Spin to keep the script running and process callbacks
    rospy.spin()

if __name__ == '__main__':
    try:
        turtle_pose_subscriber()
    except rospy.ROSInterruptException:
        pass
