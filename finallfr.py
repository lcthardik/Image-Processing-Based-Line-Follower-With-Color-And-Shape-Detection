##from __future__ import print_function
from imutils.video.pivideostream import PiVideoStream
#from imutils.video import FPS
#from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import cv2
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)

Motor1A= 8 #Pin 1 of motor 1
Motor1B= 10 #Pin 2 of motor 1
Motor1E= 12 #Enable pin of motor 1
Motor2A= 11 #Pin 1 of motor 2
Motor2B= 13 #Pin 2 of motor 2
Motor2E= 15 #Enable pin of motor 2

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)


pwmleft=GPIO.PWM(Motor1E,1000)
pwmright=GPIO.PWM(Motor2E,1000)
pwmleft.start(100)
pwmright.start(100)
#pwmleft.ChangeDutyCycle(60)
#pwmright.ChangeDutyCycle(60)

def Forward():
    

    GPIO.output(Motor1A,GPIO.HIGH)   ##motor 1
    GPIO.output(Motor1B,GPIO.LOW)  ##
    GPIO.output(Motor2A,GPIO.HIGH)   ##motor 2
    GPIO.output(Motor2B,GPIO.LOW)  ##

def Left():
    

    GPIO.output(Motor1A,GPIO.LOW)   ##motor 1
    GPIO.output(Motor1B,GPIO.HIGH)  ##
    GPIO.output(Motor2A,GPIO.HIGH)   ##motor 2
    GPIO.output(Motor2B,GPIO.LOW)  ##

def hLeft():
    
   # pwmright.start(35)
    GPIO.output(Motor1A,GPIO.HIGH)   ##motor 1
    GPIO.output(Motor1B,GPIO.LOW)  ##
    GPIO.output(Motor2A,GPIO.LOW)   ##motor 2
    GPIO.output(Motor2B,GPIO.LOW)  ##

def Right():
    

    GPIO.output(Motor1A,GPIO.HIGH)   ##motor 1
    GPIO.output(Motor1B,GPIO.LOW)  ##
    GPIO.output(Motor2A,GPIO.LOW)   ##motor 2
    GPIO.output(Motor2B,GPIO.HIGH)  ##

def hRight():
    
   # pwmleft.start(35)
    GPIO.output(Motor1A,GPIO.LOW)   ##motor 1
    GPIO.output(Motor1B,GPIO.LOW)  ##
    GPIO.output(Motor2A,GPIO.HIGH)   ##motor 2
    GPIO.output(Motor2B,GPIO.LOW)  ##



def Stop():
    

    GPIO.output(Motor1A,GPIO.LOW)   ##motor 1
    GPIO.output(Motor1B,GPIO.LOW)  ##
    GPIO.output(Motor2A,GPIO.LOW)   ##motor 2
    GPIO.output(Motor2B,GPIO.LOW)



cap = PiVideoStream(resolution=(180,180)).start()
#cap.set(3, 160)
#cap.set(4, 120)




    
    
