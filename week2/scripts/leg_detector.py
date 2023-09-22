#!/usr/bin/env python

import rospy
import tf2_ros
import geometry_msgs.msg
from people_msgs.msg import PositionMeasurementArray

def leg_detection_callback(msg):
    br = tf2_ros.TransformBroadcaster()

    for person in msg.people:
        transform = geometry_msgs.msg.TransformStamped()

        transform.header.stamp = rospy.Time.now()
        transform.header.frame_id = "base_link"
        transform.child_frame_id = "leg_" + person.name

        
        transform.transform.translation.x = person.pos.x
        transform.transform.translation.y = person.pos.y
        transform.transform.translation.z = 0.0


        transform.transform.rotation.x = 0
        transform.transform.rotation.y = 0
        transform.transform.rotation.z = 0
        transform.transform.rotation.w = 1

        br.sendTransform(transform)

if __name__ == '__main__':
    rospy.init_node('leg_broadcaster')
    rospy.Subscriber('/people_tracker_measurements', PositionMeasurementArray, leg_detection_callback)
    rospy.spin()


