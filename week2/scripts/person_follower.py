#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from people_msgs.msg import PositionMeasurementArray

class PersonFollower:
    def __init__(self):
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.laser_sub = rospy.Subscriber('/base_scan', LaserScan, self.laser_callback)
        self.person_sub = rospy.Subscriber('/people_tracker_measurements', PositionMeasurementArray, self.person_callback)
        self.person_position = None

    def laser_callback(self, msg):
        move_cmd = Twist()

        halfway_index = len(msg.ranges) // 2
        left_scan = msg.ranges[:halfway_index]
        right_scan = msg.ranges[halfway_index:]

        if self.person_position:
            move_cmd.linear.x = 0.5 
            error_angle = self.person_position.pose.pose.position.y
            move_cmd.angular.z = -1.0 * error_angle

            if min(left_scan) < 1.0 and error_angle < 0:
                move_cmd.angular.z = -1
                move_cmd.linear.x = 0
            elif min(right_scan) < 1.0 and error_angle > 0:
                move_cmd.angular.z = 1
                move_cmd.linear.x = 0

        self.cmd_pub.publish(move_cmd)

    def person_callback(self, msg):
        if msg.people:
            self.person_position = msg.people[0]

if __name__ == '__main__':
    rospy.init_node('person_follower')
    follower = PersonFollower()
    rospy.spin()
