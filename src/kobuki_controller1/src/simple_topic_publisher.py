#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node("kobukiMove")

pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

rate = rospy.Rate(2) #10 Hz

pos = Twist()
"""
Guide to understand:
http://wiki.ros.org/turtlesim/Tutorials/Moving%20in%20a%20Straight%20Line

n this case, the robot uses a differential drive plugin to move. 
That is, the robot can only move linearly in the x axis, 
or rotationaly in the angular z axis. 
This means that the only values that you need to fill in the Twist
message are the linear x and the angular z.
"""
#ir en circulos
pos.linear.x = 0.5
pos.linear.y = 0
pos.linear.z = 0
pos.angular.x = 0
pos.angular.y = 0
pos.angular.z = 0.8

#indefinidamente
while not rospy.is_shutdown():
    pub.publish(pos)
    rate.sleep()