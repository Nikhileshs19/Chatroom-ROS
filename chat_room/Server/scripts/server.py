#!/usr/bin/python3
import rospy
from std_msgs.msg import String

def chat_callback(data):
    rospy.loginfo("[{}] {}".format(data.data.split(':')[0], data.data.split(':')[1]))
    pub.publish(data)

def chat_server():
    rospy.init_node("Server", anonymous=True)
    global pub 
    pub = rospy.Publisher("server_chat", String, queue_size=10)
    sub = rospy.Subscriber("chat", String, chat_callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        chat_server()
    except rospy.ROSInterruptException:
        pass
