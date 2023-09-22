#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move_square():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('square_move', anonymous=True)
    
    rate = rospy.Rate(1)  # 1Hz
    move_cmd = Twist()
    turn_cmd = Twist()

    # Moving forward
    move_cmd.linear.x = 4
    move_cmd.angular.z = 0.0

    # Turning by 90 degrees
    turn_cmd.linear.x = 0.0
    turn_cmd.angular.z = 90 * 3.14 / 180  # Convert 90 degrees to radians

    for _ in range(4):
        for _ in range(5):  # Move forward for 5 seconds
            pub.publish(move_cmd)
            rate.sleep()
        
        for _ in range(2):  # Turn for approximately 2 seconds to achieve ~90 degrees turn
            pub.publish(turn_cmd)
            rate.sleep()

if __name__ == '__main__':
    try:
        move_square()
    except rospy.ROSInterruptException:
        pass