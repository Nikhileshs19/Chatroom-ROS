#!/usr/bin/python3
import rospy
from std_msgs.msg import String


def chat_callback(msg):
    rospy.loginfo("{}".format(msg.data))

def client2():
    rospy.init_node('Client_2', anonymous=True)
    pub = rospy.Publisher('chat', String, queue_size=10)
    sub = rospy.Subscriber("server_chat", String, chat_callback)
    rate = rospy.Rate(10) # 10hz
    print("Enter your messages below")
    while not rospy.is_shutdown():
        user_name = "Client 2: "
        user_input = input()
        message = user_name + user_input
        pub.publish(message)
        rate.sleep()


if __name__ == '__main__':
    try:
        client2()
    except rospy.ROSInterruptException:
        pass
