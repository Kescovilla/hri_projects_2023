#!/usr/bin/python3

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState

pub = rospy.Publisher('tts/phrase', String, queue_size=10)
nao_pub = rospy.Publisher('joint_states', JointState, queue_size=10)

message = ""

def listen(msg):
    message = ""
    print("I heard" + msg.data)
    message = msg.data

def publish_joint_states(joint_names, positions):
    joint_state = JointState()
    joint_state.header.stamp = rospy.Time.now()
    joint_state.name = joint_names
    joint_state.position = positions
    joint_state.velocity = []
    joint_state.effort = []
    nao_pub.publish(joint_state)

if __name__ == '__main__':
    try:
        rospy.init_node('listen_repeat', anonymous=True)
        sub = rospy.Subscriber('/speech_recognition/final_result', String, listen)
        rate = rospy.Rate(10)

    joint_names = [
        "HeadYaw", "HeadPitch", "LHipYawPitch", "LHipRoll", "LHipPitch", "LKneePitch", "LAnklePitch",
        "LAnkleRoll", "RHipYawPitch", "RHipRoll", "RHipPitch", "RKneePitch", "RAnklePitch", "RAnkleRoll",
        "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand", "RShoulderPitch",
        "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand", "RFinger23", "RFinger13", "RFinger12",
        "LFinger21", "LFinger13", "LFinger11", "RFinger22", "LFinger22", "RFinger21", "LFinger12", "RFinger11",
        "LFinger23", "LThumb1", "RThumb1", "RThumb2", "LThumb2"
    ]
    keyframe1 = [
        -0.15225391, -0.671952, 0.00404327520000014, -3.8051500000024774e-05, 1.9148000000024368e-05,
        -0.0021483938900000027, -0.00016097489999999937, -1.490230000000814e-05, 0.00404327520000014,
        -0.14456097049999994, 1.9148000000024368e-05, 0.005127703179999998, -4.8639999999711137e-05,
        0.0005982787999998518, -1.172980808, 1.0188358124999999, 0.021690968000000144, -0.86841936814,
        -0.702919498, 0.5417, 0.0, 0.3141590000000001, -0.15225391, 1.45811342218, 1.82387, 0.0, 0.0, 0.0, 0.0,
        0.5416452882999999, 0.5416452882999999, 0.5416452882999999, 0.0, 0.5416452882999999, 0.0, 0.5416452882999999,
        0.0, 0.5416452882999999, 0.5416452882999999, 0.0, 0.0, 0.5416452882999999
    ]

    keyframe2 = [
        -1.287275524, 0.48674427119999997, 0.4283950752000001, -0.13013037549999998, 0.04869801500000004,
        1.04274324292, -0.7543636740000002, -0.06465301850000005, 0.4283950752000001, 0.14381814700000006,
        -0.5386801809999999, 1.09301445904, -0.05660741019999982, 0.3211053278999999, -0.7120477380000001,
        0.8705247588999998, 0.18353896000000036, -0.41671311885999995, 0.390672954, 0.5251, 1.654770578,
        -0.6344411238, 1.4261811459999998, 0.84215035498, 1.1461199080000004, 0.3017, 0.30166952830000004,
        0.30166952830000004, 0.30166952830000004, 0.5250469649, 0.5250469649, 0.5250469649, 0.30166952830000004,
        0.5250469649, 0.30166952830000004, 0.5250469649, 0.30166952830000004, 0.5250469649, 0.5250469649,
        0.30166952830000004, 0.30166952830000004, 0.5250469649
    ]

        while not rospy.is_shutdown():
            if message == 'dance':
                # Dance keyframe 1
                publish_joint_states(joint_names, keyframe1)
                rospy.sleep(2)
                # Dance keyframe 2
                publish_joint_states(joint_names, keyframe2)
                rospy.sleep(2)

            message = ""
            rate.sleep()

        rospy.spin()
    except rospy.ROSInterruptException:
        pass
