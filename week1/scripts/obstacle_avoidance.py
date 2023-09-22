#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoidance:
    def __init__(self):
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.laser_sub = rospy.Subscriber('/base_scan', LaserScan, self.laser_callback)

    def laser_callback(self, msg):
        move_cmd = Twist()

        halfway_index = len(msg.ranges) // 2
        left_scan = msg.ranges[:halfway_index]
        right_scan = msg.ranges[halfway_index:]

        if min(left_scan) < 1.0:
            move_cmd.angular.z = -1
        elif min(right_scan) < 1.0:
            move_cmd.angular.z = 1
        else:
            move_cmd.linear.x = 1

        self.cmd_pub.publish(move_cmd)

if __name__ == '__main__':
    rospy.init_node('obstacle_avoidance')
    obstacle_avoider = ObstacleAvoidance()
    rospy.spin()
