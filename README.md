Task to create a chatroom for 3 users to send and view messages using ROS

I have done the task by creating 3 client nodes and a server node, all of which are both subscribers and publishers.
The three client nodes publish the user input string on /chat, which the server subscribes to, and keeps a log of the chat of all the users.

The server then publishes all the data it gets from the /chat topic onto the /server_chat topic, which each client node subscribes to, getting the chat of all the messages on their screen.

ROS Topics published:
/chat
/server_chat

ROS Messages and Services:
std_msgs is used (custom messages lead to certain errors)
No services are being used in this

RQT Graph:
![chatroom](https://user-images.githubusercontent.com/117987806/215200978-94ac612d-0fda-4fcf-a6e1-9ca63ddd0d2e.png)

Screen-recorded video:
https://www.youtube.com/watch?v=ZGEIencCR3s
