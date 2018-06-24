#! /usr/bin/env python

import rospy
from kobuki_controller1.msg import Age

def main():
    rospy.init_node("robot_age")
    
    pub = rospy.Publisher("/robotAge_topic", Age, queue_size=1)
    
    rate = rospy.Rate(2)
    
    age = Age()
    
    age.year = 1 #Fill the values of the message
    age.month = 2 #Fill the values of the message
    age.day = 12 #Fill the values of the message
    
    while not rospy.is_shutdown():
        pub.publish(age)
        rate.sleep()
        
if __name__=='__main__':
    main()