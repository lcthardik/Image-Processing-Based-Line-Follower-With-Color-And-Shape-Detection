from picamera import PiCamera
import argparse as ap
import imutils as im
import time
import cv2
import LED
import numpy as np
import math
import findCMExpensive as CM
#import lfr as lf
import overlay as ol
import RPi.GPIO as GPIO
from threading import Thread
import csvreader as csv
from imutils.video.pivideostream import PiVideoStream
csv.CSVInitialize()
ol.setFiles(csv.CSVRead())
vs=PiVideoStream(resolution=(640,480)).start()
frame=vs.read()
time.sleep(1.0)
frame=vs.read()
shape,color,number_of_shapes=CM.getColor(frame)
ol.overlay(color,shape,number_of_shapes)
ol.showPlantation()
cv2.waitKey(0)
cv2.destroyAllWindows()
LED.blinkLED(color,number_of_shapes)
vs.stop()
