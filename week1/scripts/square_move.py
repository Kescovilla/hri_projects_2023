#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move_square():
    rospy.init_node('move_square', anonymous=True)
    rate = rospy.Rate(1)  # 1 Hz, adjust as needed

    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    cmd_vel_msg = Twist()

    side_length = 1.0 

    FORWARD = 0
    TURN = 1

    state = FORWARD
    forward_duration = 2  
    turn_duration = 2

    while not rospy.is_shutdown():
        if state == FORWARD:
            cmd_vel_msg.linear.x = 2.0  
            cmd_vel_msg.angular.z = 0.0
            cmd_vel_pub.publish(cmd_vel_msg)
            forward_duration -= 1

            if forward_duration == 0:
                state = TURN
                forward_duration = 2  

        elif state == TURN:
            cmd_vel_msg.linear.x = 0.0
            cmd_vel_msg.angular.z = 2.0
            cmd_vel_pub.publish(cmd_vel_msg)
            turn_duration -= 1

            if turn_duration == 0:
                state = FORWARD
                turn_duration = 2  

        rate.sleep()

    cmd_vel_msg.linear.x = 0.0
    cmd_vel_msg.angular.z = 0.0
    cmd_vel_pub.publish(cmd_vel_msg)

if __name__ == '__main__':
    try:
        move_square()
    except rospy.ROSInterruptException:
        pass
