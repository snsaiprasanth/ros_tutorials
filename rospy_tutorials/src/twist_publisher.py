#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist  # Import the Twist message type

def turtle_twist_publisher():
    # Initialize the ROS node
    rospy.init_node('turtle_twist_publisher', anonymous=True)

    # Create a publisher for the turtle velocity (Twist) on the "/turtle1/cmd_vel" topic
    twist_publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    # Create a Twist message
    twist_msg = Twist()

    # Set linear and angular velocities
    twist_msg.linear.x = 1.0  # linear velocity in the x-axis
    twist_msg.angular.z = 1.0  # angular velocity around the z-axis

    # Set the loop rate (adjust as needed)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        # Publish the Twist message
        twist_publisher.publish(twist_msg)

        # Sleep to meet the specified loop rate
        rate.sleep()

if __name__ == '__main__':
    try:
        turtle_twist_publisher()
    except rospy.ROSInterruptException:
        pass
