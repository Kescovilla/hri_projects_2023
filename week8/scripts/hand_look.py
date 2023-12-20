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

# Looks at hand. Keyframe obtained by using rostopic echo /joint_states in terminal + some minor tweaking
# I learned a little later (like 2 days before deadline) from one of the dudes in the class that it should move frames?

# Wonky Looking
keyframe1 = [
    0.24777759600000016, -9.093359999989836e-05, -0.00010594240000005861, -3.8051500000024774e-05,
    -0.00018283900000004571, -0.00016400378000000493, -0.00016097489999999937, -1.490230000000814e-05,
    -0.00010594240000005861, 0.0034307470000000118, -0.00018283900000004571, -0.0008254671499999949,
    -0.0032260989999999268, -0.0001017730000000272, 0.02294236999999999, 0.14324278919999994, -0.52767451,
    -1.0535102309800002, -1.82387, 0.0, 1.568840974, -0.0444781273999999, 0.40545424799999985, 0.0349066,
    0.2918191999999997, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
]

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

    publish_keyframe(keyframe1)
    #added delay
    rospy.sleep(5.0)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
