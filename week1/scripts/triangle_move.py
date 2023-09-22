#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move_triangle():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('triangle_move', anonymous=True)
    rate = rospy.Rate(1) # 1 Hz

    # Initialize a Twist message
    move_cmd = Twist()

    for _ in range(3):
        # Forward motion
        move_cmd.linear.x = 0.5
        move_cmd.angular.z = 0
        pub.publish(move_cmd)
        rospy.sleep(5)

        # Turn by 120 degrees (2π/3 radians)
        move_cmd.linear.x = 0
        move_cmd.angular.z = 0.5
        pub.publish(move_cmd)
        rospy.sleep(2 * 3.14159 / 3 / 0.5)

    # Stop the robot
    move_cmd.linear.x = 0
    move_cmd.angular.z = 0
    pub.publish(move_cmd)

    rate.sleep()

if __name__ == '__main__':
    try:
        move_triangle()
    except rospy.ROSInterruptException:
        pass