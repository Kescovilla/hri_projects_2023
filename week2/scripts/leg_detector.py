#!/usr/bin/env python3

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped
from people_msgs.msg import PositionMeasurementArray
import tf_conversions

#This certainly detects something.... Probably the wrong thing
def leg_detect(msg):
    global goal

    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "odom"
    t.child_frame_id = "legs"

    if len(msg.people) == 0:
        print("nothing detected?")
        return None

    t.transform.translation.x = msg.people[0].pos.x
    t.transform.translation.y = msg.people[0].pos.y
    t.transform.translation.z = msg.people[0].pos.z
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, math.pi/2)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    br.sendTransform(t)

    print(f"location: {t.transform.translation.z}")

if __name__ == '__main__':
    try:
        rospy.init_node('leg_detector')
        tf_broadcaster = tf2_ros.TransformBroadcaster()
        leg_detector_topic = "/people_tracker_measurements"
        rospy.Subscriber(leg_detector_topic, PositionMeasurementArray, leg_detect)

        rospy.spin()
    except rospy.ROSInterruptException:
        pass
