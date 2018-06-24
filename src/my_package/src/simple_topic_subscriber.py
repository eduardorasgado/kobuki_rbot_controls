#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callbackFunction(mesg):
    message = "The counter goes: {}".format(mesg.data)
    rospy.loginfo(message)

def main():
    rospy.init_node("topic_subscriber")
    
    sub = rospy.Subscriber("counter", Int32, callbackFunction)
    
    rospy.spin()
    
if __name__ == '__main__':
    main()