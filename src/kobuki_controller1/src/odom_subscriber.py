#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry 

def odomCallback(msg):
    linearmsg = "the linear odom is: {}".format(msg.twist.twist.linear)
    angularmsg = "the angular odom is: {}".format(msg.twist.twist.angular)
    rospy.loginfo(linearmsg)
    rospy.loginfo(angularmsg)
    
def main():
    rospy.init_node("odom_reader")
    
    subscriber = rospy.Subscriber("/odom", Odometry, odomCallback)
     
    rospy.spin()

if __name__ == '__main__':
    main()