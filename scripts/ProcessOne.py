#! /usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from assignment1.srv import *
import random

def randMtoN(M,N):
	return M + (random.randint(0,10000) / (10000 / (N-M)) ) 

def myrandom(req):

	resp = valuesResponse()

	resp.a = randMtoN(req.min, req.max)
	resp.b = randMtoN(req.min, req.max)

	rospy.loginfo("Random target received [%.2f, %.2f]" %(resp.a, resp.b))
	return resp

def main():
   
   rospy.init_node('randomTarget_server')
   rospy.Service('random_target', values, myrandom)

   rospy.spin()

if __name__ == '__main__':
	main()
