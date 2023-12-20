#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

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

keyframe3 = [
    1.5871948699999998, -0.5676301704, -0.8972799479999999, 0.07612211300000005, -0.955177375,
    1.7941656312400003, 0.7517185011, 0.445801419, -0.8972799479999999, -0.32191705249999997,
    -0.2506467189999999, 1.8153324590800002, -0.7137059313999999, -0.3235257046000001,
    -1.0557661539999998, 0.5676683375, 0.593998816, -0.08714268364, 1.6152192719999998, 0.3711,
    0.06549003800000008, -0.7350104554999999, 0.24777759600000016, 0.691631929, 0.3625853560000001,
    0.0803, 0.0802918897, 0.0802918897, 0.0802918897, 0.37106251889999997, 0.37106251889999997,
    0.37106251889999997, 0.0802918897, 0.37106251889999997, 0.0802918897, 0.37106251889999997,
    0.0802918897, 0.37106251889999997, 0.37106251889999997, 0.0802918897, 0.0802918897,
    0.37106251889999997
]




# Create a ROS Publisher for the /joint_states topic
joint_states_pub = rospy.Publisher('/joint_states', JointState, queue_size=10)

def publish_keyframe(keyframe):
    joint_state = JointState()
    joint_state.header = Header()
    joint_state.header.frame_id="torso"
    joint_state.header.stamp = rospy.Time.now()
    joint_state.name = joint_names
    joint_state.position = keyframe
    joint_states_pub.publish(joint_state)

def main():
    rospy.init_node('nao_keyframe_animation')

    rate = rospy.Rate(30)

    while not rospy.is_shutdown():
        #VERY wonky animation. Could not get interpolated/smoother frames to run properly. Tested out different hz, and FPS inside my RVIZ
        #Learned a lot on how general key frame animation works though (Just not on ROS). So that's nice.
        publish_keyframe(keyframe1)
        rate.sleep()
        publish_keyframe(keyframe2)
        rate.sleep()
        publish_keyframe(keyframe3)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
