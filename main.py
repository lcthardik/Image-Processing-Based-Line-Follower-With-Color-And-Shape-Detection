from __future__ import print_function
from imutils.video.pivideostream import PiVideoStream
import argparse as ap
import imutils as im
import time
import cv2
import LED
import numpy as np
import math
import csvreader as csv
import findCMExpensive as CM
import lfr as lf
import overlay as ol
import RPi.GPIO as GPIO

csv.CSVInitialize()
mean_position = k = n = 0
ol.setFiles(csv.CSVRead())
vs = PiVideoStream().start()
frame = vs.read()
time.sleep(2.0)
stop = 0
mean_position = k = n = front_error = k2 = n2 = 0

while stop == 0:
    frame = vs.read()
    cv2.waitKey(1)
    mean_position, thickness = lf.calculateError(frame, 200)
    front_error, thickness = lf.calculateError(frame, 40)

    if (mean_position > 130 and mean_position < 190) and \
            (front_error > 130 and front_error < 190) and thickness < 100:
        lf.setMode('high')
    else:
        lf.setMode('low')

    if (mean_position > 130 and mean_position < 190) and \
            thickness > 100 and thickness < 310:
        print('CM detected')
        cv2.destroyAllWindows()

        while thickness > 100:
            frame = vs.read()
            cv2.waitKey(1)
            mean_position, thickness = lf.calculateError(frame)
            lf.PID(mean_position)

        print('motorspeed set to 0')
        lf.set_motor_speed(0.0, 0.0)
        time.sleep(1.0)
        print('Now detecting color markers')
        shape, color, number_of_shapes = CM.getColor(frame)

        if number_of_shapes == 0:
            lf.setInvertedMode(1)
        else:
            lf.setInvertedMode(0)
            LED.addColor(color)
            print('color:', color, 'shape:', shape, 'number:', number_of_shapes)
            ol.overlay(color, shape, number_of_shapes)
            ol.showPlantation()
            LED.blinkLED(color, number_of_shapes)
            lf.useLastState()
            time.sleep(1.0)
    elif thickness == 320:
        print('Stop detected')
        stop = 1
    elif thickness == 0:
        lf.useLastState()
    else:
        print('Executing PID')
        lf.PID(mean_position)

LED.blinkLEDFinal()
cv2.waitKey(0)
cv2.destroyAllWindows()
GPIO.cleanup()
