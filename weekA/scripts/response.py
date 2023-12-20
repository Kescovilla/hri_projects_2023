import rospy
from std_msgs.msg import String

# Global variables to store the received message
message = ""
response_received = False

def listen(msg):
    global message, response_received
    message = msg.data.lower()  # Convert to lowercase for easier comparison
    response_received = True

def ask_question(question):
    global response_received
    pub.publish(question)
    response_received = False
    while not response_received and not rospy.is_shutdown():
        rospy.sleep(0.1)  # Wait for a response

if __name__ == '__main__':
    try:
        rospy.init_node('decision_helper', anonymous=True)
        pub = rospy.Publisher('tts/phrase', String, queue_size=10)
        sub = rospy.Subscriber('/speech_recognition/final_result', String, listen)

        ask_question("Do you need it?")
        if "yes" in message:
            ask_question("Do you REALLY need it?")
            if "yes" in message:
                pub.publish("Alright, if you really need it, go for it!")
            else:
                pub.publish("Well, if you're not sure, maybe give it a bit more thought.")
        else:
            pub.publish("Are you sure you don't need it? Sometimes we don't know what we need!")

        rospy.spin()
    except rospy.ROSInterruptException:
        pass
