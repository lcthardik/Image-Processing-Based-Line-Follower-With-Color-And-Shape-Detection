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
pwmleft.start(90)
pwmright.start(90)
stop=0
cap = PiVideoStream(resolution=(180,180)).start()
ar=0
cx=0
num=0
#pwmleft.ChangeDutyCycle(60)
#pwmright.ChangeDutyCycle(60)


def stoprobo():
    global pwmleft,pwmright
    pwmleft.ChangeDutyCycle(0)
    pwmright.ChangeDutyCycle(0)
def startrobo():
    global pwmleft,pwmright
    pwmright.ChangeDutyCycle(90)
    pwmleft.ChangeDutyCycle(90)
def init():
    startrobo()
    global cap
    #cap = vs
    
    frame =cap.read()
    time.sleep(2.0)
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


def straight():
    Forward()

#cap.set(3, 160)
#cap.set(4, 120)
def stoplfr():
    global stop
    stoprobo()
    stop=1
def startlfr():
    print 'inside start LFR'
    global stop,cap,cx,ar,num
    startrobo()
    stop=0
    while stop==0:
        frame =cap.read()
        #cv2.imshow('frame',frame)
        crop_img = frame[60:120, :]
        gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        ret,thresh1 = cv2.threshold(gray,60,255,cv2.THRESH_BINARY_INV)
        mask = cv2.erode(thresh1, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        im2,contours,hierarchy = cv2.findContours(mask.copy(), 1, cv2.CHAIN_APPROX_NONE)
        num=len(contours)
        if num > 0:
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.line(crop_img,(cx,0),(cx,720),(255,0,0),1)
            cv2.line(crop_img,(0,cy),(1280,cy),(255,0,0),1)
            cv2.drawContours(crop_img, contours, -1, (0,255,0), 1)
            #print(cy)
            ar=cv2.contourArea(c)
            #print(ar)
            if cx >= 60 and cx <=120:
                Forward()
                
            if cx > 120 and cx< 155 :
                hRight()
                
            if cx>20 and cx < 60:

                hLeft()

            if cx>= 155 :
                
                Left()  

            if cx<=20:

                Right()

            if cx>110 and cy>=40:

                Left()

            if cx<70 and cy>=40:
                
                Right()
                
            else:

                pass

     
        #cv2.imshow('frame',crop_img)
        if stop==1:
            
            break


def startlfrinverted():
    print 'executing inverted'
    global stop,cap,cx,ar,num
    startrobo()
    stop=0
    while stop==0:
        frame =cap.read()
        #cv2.imshow('frame',frame)
        crop_img = frame[60:120, :]
        gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        ret,thresh1 = cv2.threshold(gray,60,255,cv2.THRESH_BINARY)
        mask = cv2.erode(thresh1, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        #x=np.count_nonzero(thresh1[178:179,:])
        #print x
        #if x>50:

        #    print 'Inverted region'
        #    thresh1=255-thresh1
        #else:
        #    pass
        im2,contours,hierarchy = cv2.findContours(mask.copy(), 1, cv2.CHAIN_APPROX_NONE)
        num=len(contours)
        if num > 0:
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.line(crop_img,(cx,0),(cx,720),(255,0,0),1)
            cv2.line(crop_img,(0,cy),(1280,cy),(255,0,0),1)
            cv2.drawContours(crop_img, contours, -1, (0,255,0), 1)
            #print(cy)
            ar=cv2.contourArea(c)
            #print(ar)
            if cx >= 60 and cx <=120:
                Forward()
                
            if cx > 120 and cx< 155 :
                hRight()
                
            if cx>20 and cx < 60:

                hLeft()

            if cx>= 155 :
                
                Left()  

            if cx<=20:

                Right()

            if cx>110 and cy>=40:

                Left()

            if cx<70 and cy>=40:
                
                Right()
                
            else:

                pass

     
        #cv2.imshow('frame',crop_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            
            break

    
    
