############################################################################################################
	# Team Id : PB#4097
	# Author List : Aditya Agrawal
	# Filename: Something.py
	# Theme: Planterbot
	# Functions: <Comma separated list of Functions defined in this file>
	# Global Variables: <List of global variables defined in this file, none if no global * variables>
#############################################################################################################
from __future__ import print_function
from imutils.video.pivideostream import PiVideoStream
#from imutils.video import FPS
#from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse as ap
import imutils as im
import time
import cv2
import LED
import numpy as np
import math
import findCMExpensive as CM
import lfr as lf
import overlay as ol
import RPi.GPIO as GPIO
from threading import Thread
import csvreader as csv
#import motor
#motor.initialize()
mean_position=area=0
#vs = PiVideoStream(resolution=(180,180)).start()
#frame=vs.read()
csv.CSVInitialize()
ol.setFiles(csv.CSVRead())
#time.sleep(1.0)
vs=lf.cap
stop=0
#cx_area=[0,0]
lfrstop=0
calllfr=lf.startlfr #can be lf.lfrinverted for inverted mode
def lfrfunction():
	global calllfr,lfrstop#,vs,cx_area,lfrstop
	lf.init()
	calllfr()
def CMroutine():
	global CMframe,calllfr
	print('Now detecting color markers')
	shape,color,number_of_shapes=CM.getColor(frame)
	cv2.waitKey(0)
	if number_of_shapes==0:

		calllfr=lf.startlfrinverted
	else:
		calllfr=lf.startlfr
		LED.addColor(color)
		
		print('color:',color,'shape:',shape,'number:',number_of_shapes)
		ol.overlay(color,shape,number_of_shapes)

		ol.showPlantation()
		LED.blinkLED(color,number_of_shapes)

lfrthread=Thread(target=lfrfunction,args=())
CM_overlay_LED=Thread(target=CMroutine,args=())


lfrthread.start()

while stop==0:
	frame = vs.read()
	cv2.waitKey(1)
	#cv2.imshow('frame',frame)
	#cv2.waitKey(0)
	#cv2.waitKey(2) #Uncomment waitkey if stability issues persist
	#cv2.waitKey(100)
	if lf.ar>3000 and (lf.cx>=70 and lf.cx<=110):
		#print('CM detected')
		#cv2.destroyAllWindows()
		lf.stoplfr()
		
		#while lf.area>2000:
		#	pass
		#lf.setmaxspeed(0)
		#lfrstop=1
			
		print('motorspeed set to 0')

		#lf.set_motor_speed(0.0,0.0)
		vs.stop()
		vs = PiVideoStream(resolution=(1280,720)).start()
		time.sleep(0.5)
		CMframe=vs.read()
		vs.stop()
		vs=PiVideoStream(resolution=(180,180)).start()
		lf.startlfr()
		CM_overlay_LED.start()
		
		
	elif lf.ar>10000:
		print('Stop detected')
		lf.stoplfr()
		stop=1
	else:
		pass
	#lf.PID(mean_position)
	#cv2.waitKey(1)
LED.blinkLEDFinal()
cv2.waitKey(0)
cv2.destroyAllWindows()
GPIO.cleanup()
#ToDo
#ZI Screenshot			
#Add track end, something that will set the stop flag
#Track start motor run
#Motor run after detect CM
#Multithreading
