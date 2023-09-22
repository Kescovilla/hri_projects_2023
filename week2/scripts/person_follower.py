#!/usr/bin/env python3

import rospy
import tf2_ros
from geometry_msgs.msg import Twist, TransformStamped
from sensor_msgs.msg import LaserScan
from tf.transformations import euler_from_quaternion
import numpy as np
import math

global laser_data

def laser_callback(data):
    global laser_data 
    laser_data = data

def avoid_obstacle(msg):
    if (msg.linear.x <= 0.01 and abs(msg.angular.z) <= 0.01):
        msg.linear.x = 0
        msg.angular.z = 0
    else:
        min_distance = min(laser_data.ranges)
        if min_distance < 0.5: 
            msg.linear.x = 0.0
        elif msg.linear.x + 0.5 < min_distance:
            msg.linear.x += 0.5
        
        if min_distance < 1.0:  
            left_distances = sum(laser_data.ranges[:len(laser_data.ranges)//2])
            right_distances = sum(laser_data.ranges[len(laser_data.ranges)//2:])
            
            if left_distances < right_distances:
                msg.angular.z = 0.5  # Turn right
            else:
                msg.angular.z = -0.5  # Turn left

    cmd_vel_publisher.publish(msg)
    return msg

def follow_person_legs():
    rospy.init_node('follow_person_legs', anonymous=True)
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)
    rate = rospy.Rate(10)  # 10 Hz - should this be 1? idk
    transform = TransformStamped()

    while not rospy.is_shutdown():
        msg = Twist()
        try:
            transform = tfBuffer.lookup_transform('base_link', 'person', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            print("me not working")
            rate.sleep()
            continue

        (roll, pitch, yaw) = euler_from_quaternion([transform.transform.rotation.x, transform.transform.rotation.y, transform.transform.rotation.z, transform.transform.rotation.w])

        print(np.linalg.norm(np.array([transform.transform.translation.x, transform.transform.translation.y, transform.transform.translation.z])))
        msg.linear.x = 0.2 * np.linalg.norm(np.array([transform.transform.translation.x, transform.transform.translation.y]))
        msg.angular.z = yaw

        msg = avoid_obstacle(msg)

        rate.sleep()

if __name__ == '__main__':
    try:
        cmd_vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        laser_sub = rospy.Subscriber('/base_scan', LaserScan, laser_callback)
        follow_person_legs()
    except rospy.ROSInterruptException:
        pass
