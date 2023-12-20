#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan  # Import the correct message type

# Global variable to store the closest distance
closest_distance = float('inf')

def callback(data):
    global closest_distance

    # Extract the laser scan data
    laser_data = data.ranges

    # Loop through the laser scan data to find the closest reading
    for distance in laser_data:
        if distance < closest_distance:
            closest_distance = distance

    # Print the closest distance
    rospy.loginfo('Closest distance: %f', closest_distance)

def listener():
    global closest_distance

    rospy.init_node('base_listener', anonymous=True)

    # Subscribe to the /base_scan topic with the correct message type
    rospy.Subscriber('/base_scan', LaserScan, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
