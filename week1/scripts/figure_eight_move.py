#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def figure_eight_move():
    rospy.init_node('figure_eight_move', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    
    rate = rospy.Rate(1)  # 1 Hz
    move_cmd = Twist()
    
    while not rospy.is_shutdown():
        # Move forward
        move_cmd.linear.x = 0.5
        move_cmd.angular.z = 0
        pub.publish(move_cmd)
        rospy.sleep(1)  # Adjust this value as necessary
        
        # Turn in one direction
        move_cmd.linear.x = 0
        move_cmd.angular.z = 0.5
        pub.publish(move_cmd)
        rospy.sleep(1)  # Adjust this value as necessary

        # Move forward again
        move_cmd.linear.x = 0.5
        move_cmd.angular.z = 0
        pub.publish(move_cmd)
        rospy.sleep(1)  # Adjust this value as necessary
        
        # Turn in the opposite direction
        move_cmd.linear.x = 0
        move_cmd.angular.z = -0.5
        pub.publish(move_cmd)
        rospy.sleep(1)  # Adjust this value as necessary
        
        rate.sleep()

if __name__ == '__main__':
    try:
        figure_eight_move()
    except rospy.ROSInterruptException:
        pass