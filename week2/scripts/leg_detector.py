#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import TransformStamped
from people_msgs.msg import PositionMeasurementArray
import tf_conversions
from tf2_ros import TransformBroadcaster

def leg_detector(data):
    for each in data.people:
        if each.header.frame_id == "odom":
            transform = TransformStamped()
            transform.header.stamp = rospy.Time.now()
            transform.header.frame_id = "odom"
            transform.child_frame_id = "person"
            
            transform.transform.translation.x = each.pos.x
            transform.transform.translation.y = each.pos.y
            transform.transform.translation.z = 0.0  #legs shouldn't be moving on the z-axis
            
            q = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
            transform.transform.rotation.x = q[0]
            transform.transform.rotation.y = q[1]
            transform.transform.rotation.z = q[2]
            transform.transform.rotation.w = q[3]
            
            tf_broadcaster.sendTransform(transform)

if __name__ == '__main__':
    try:
        rospy.init_node('leg_detector')
        tf_broadcaster = TransformBroadcaster()
        leg_detector_topic = "/people_tracker_measurements"
        rospy.Subscriber(leg_detector_topic, PositionMeasurementArray, leg_detector)

        rospy.spin()
    except rospy.ROSInterruptException:
        pass
