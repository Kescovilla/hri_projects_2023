#!/usr/bin/env python


import rospy
from sensor_msgs.msg import LaserScan


def callback(data):
    # Assuming the LaserScan message might have 'inf' values, we filter them out
    valid_readings = [reading for reading in data.ranges if reading != float('inf')]
    
    # Check if there are valid readings
    if valid_readings:
        closest_reading = min(valid_readings)
        rospy.loginfo("Closest reading: %f", closest_reading)
    else:
        rospy.loginfo("No valid laser readings received.")


def listener():
    # Initialize the node as before
    rospy.init_node('base_scan_listener', anonymous=True)
    
    # Subscribe to the /base_scan topic instead of 'chatter'
    rospy.Subscriber("/base_scan", LaserScan, callback)
    
    # Keep the node alive as before
    rospy.spin()


if __name__ == '__main__':
    listener()





