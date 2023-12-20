#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def speech_callback(msg):
    rospy.loginfo("I heard this: " + msg.data)
    tts_publisher.publish(msg.data)

if __name__ == '__main__':
    rospy.init_node('speech_echo_node')

    # Subscriber for speech recognition results
    rospy.Subscriber('/speech_recognition/final_result', String, speech_callback)

    # Publisher for text-to-speech
    tts_publisher = rospy.Publisher('tts/phrase', String, queue_size=10)

    rospy.spin()
