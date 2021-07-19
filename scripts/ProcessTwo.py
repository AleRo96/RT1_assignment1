#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from assignment1.srv import *
import random

k = 4
x = 0.0
y = 0.0
distance_x = 0.0
distance_y = 0.0
target = Odometry()

def clbk_odm(msg):
   global x, y, distance_x, distance_y, target
   
   rospy.wait_for_service('random_target')

   x = msg.pose.pose.position.x
   y = msg.pose.pose.position.y
   

   distance_x = target.pose.pose.position.x - x
   distance_y = target.pose.pose.position.y - y

   if (distance_x > -0.1 and distance_x < 0.1) and (distance_y > -0.1 and distance_y < 0.1): 
	 
	 req = valuesRequest()
	 req.min = -6
	 req.max = 6

	 resp = client(req)

	 target.pose.pose.position.x = resp.a
	 target.pose.pose.position.y = resp.b 
	 rospy.loginfo("Goal reached!")
	 
   else:
	
	twist_msg = Twist()
	twist_msg.linear.x = (k* distance_x)
	twist_msg.linear.y = (k* distance_y)
	pub.publish(twist_msg)


def main():
   global pub, client

   rospy.init_node('robot_controller', anonymous = True)

   sub = rospy.Subscriber('/odom', Odometry, clbk_odm)
   client = rospy.ServiceProxy('random_target', values)
   pub = rospy.Publisher('/cmd_vel',Twist, queue_size=1)
   
   
   rate = rospy.Rate(20)

   rospy.spin()

if __name__ == '__main__':
    main()
