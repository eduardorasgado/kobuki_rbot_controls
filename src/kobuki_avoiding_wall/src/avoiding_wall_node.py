#! /usr/bin/env python
#publisher to /cmd_vel
#subscriber to /kobuki/laser/scan

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class scanMonitor:
    def __init__(self, pub):
        self._pub = pub
    
    def scanCallback(self, msg):
        #msg.ranges here is our sensing
        #the robot movement instruction object
        movement = Twist()
        
        movement.linear.x = 0.8
        movement.linear.y = 0
        movement.linear.z = 0
        
        movement.angular.x = 0
        movement.angular.y = 0
        movement.angular.z = 0
        
        #print(len(msg.ranges))
        minRange = min(msg.ranges)
        
        for i in range(len(msg.ranges)):
            #if robot detects something not infinite or zero
            if msg.ranges[i] != 0 and msg.ranges[i] != float('Inf'):
                #rangingMSG = "range #{}: {}".format(i, msg.ranges[i])
                #rospy.loginfo(rangingMSG)
                #looking for the minimum value index
                if minRange == msg.ranges[i]:
                    #specting been at least 2 meters near the obstacle
                    if minRange <= 2.0:
                        rospy.loginfo(msg.ranges[i])
                        angle = i/2
                        angleMSG = "The angle of min is: {} deg".format(angle)
                        rospy.loginfo(angleMSG)
                        #changing the angula spin
                        movement.angular.z = 0.8
                        #decreasing the velocity
                        movement.angular.x = 1 - (minRange*0.1)
        
        #publishing the movements
        self._pub.publish(movement)

def main():
    #we create the node
    rospy.init_node('scan_and_move_node')
    
    #create the publisher--------------
    publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    scanner = scanMonitor(publisher)
    
    #Create the subscriber--------------
    rospy.Subscriber('/kobuki/laser/scan', LaserScan, scanner.scanCallback)
    
    rospy.spin()
    
if __name__=='__main__':
    main()