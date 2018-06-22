#! /usr/bin/env python
import rospy 
from geometry_msgs.msg import Twist 

rospy.init_node("kobukiStop") 

pub = rospy.Publisher('cmd_vel', Twist, queue_size=10) 
rate = rospy.Rate(2)
pos = Twist()
#parar
pos.linear.x = 0
pos.linear.y = 0
pos.linear.z = 0
pos.angular.x = 0
pos.angular.y = 0
pos.angular.z = 0

while not rospy.is_shutdown():
    pub.publish(pos)
    rate.sleep()
    
