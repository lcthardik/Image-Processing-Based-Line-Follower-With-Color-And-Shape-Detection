import RPi.GPIO as GPIO
import math
import time
import cv2
import numpy as np

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

Motor1a = 8
Motor1b = 10
Motor1e = 12
Motor2a = 11
Motor2b = 13
Motor2e = 15

kp = 0.038
ki = 0
kd = 0.4
integral = 0
last_propotional = 0
invertedmode = 0
maxi = 40
lastPwm = {'left': maxi, 'right': maxi}

GPIO.setup(Motor1a, GPIO.OUT)
GPIO.setup(Motor1b, GPIO.OUT)
GPIO.setup(Motor1e, GPIO.OUT)
GPIO.setup(Motor2a, GPIO.OUT)
GPIO.setup(Motor2b, GPIO.OUT)
GPIO.setup(Motor2e, GPIO.OUT)

pwmleft = GPIO.PWM(Motor1e, 1000)
pwmright = GPIO.PWM(Motor2e, 1000)
pwmleft.start(0)
pwmright.start(0)
kernel = np.ones((5, 5), np.uint8)

def strai():
    GPIO.output(Motor1a, GPIO.LOW)
    GPIO.output(Motor1b, GPIO.HIGH)
    GPIO.output(Motor2a, GPIO.LOW)
    GPIO.output(Motor2b, GPIO.HIGH)

def right():
    GPIO.output(Motor1a, GPIO.HIGH)
    GPIO.output(Motor1b, GPIO.LOW)
    GPIO.output(Motor2a, GPIO.LOW)
    GPIO.output(Motor2b, GPIO.HIGH)

def left():
    GPIO.output(Motor1a, GPIO.LOW)
    GPIO.output(Motor1b, GPIO.HIGH)
    GPIO.output(Motor2a, GPIO.HIGH)
    GPIO.output(Motor2b, GPIO.LOW)

def useLastState():
    global lastState, lastPwm
    lastState()
    set_motor_speed(lastPwm['left'], lastPwm['right'])

def setInvertedMode(args):
    global invertedmode
    invertedmode = args

def setMode(pwmvalue):
    global maxi, kp, kd, ki
    if pwmvalue == 'high' or pwmvalue == 'High':
        maxi = 100
        kp = 0.095
        kd = 0.9
        ki = 0
    elif pwmvalue == 'medium' or pwmvalue == 'Medium':
        maxi = 70
        kp = 0.0665
        kd = 0.665
        ki = 0
    else:
        maxi = 40
        kp = 0.038
        kd = 0.3
        ki = 0

lastState = strai

def calculateError(frame, rownumber, cumulative=0):
    global inverted, kernel

    gray_line = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresholded_line = cv2.threshold(gray_line, 127, 255, cv2.THRESH_BINARY)
    thresholded_line = cv2.morphologyEx(thresholded_line, cv2.MORPH_CLOSE, kernel)

    thresh = thresholded_line[rownumber:rownumber + 1, :]
    thresh = thresh.astype(int)
    difference_array = np.diff(thresh)
    position1 = np.argmax(difference_array)
    position0 = np.argmin(difference_array)

    if difference_array[0, position1] == 0 and thresh[319] == 0:
        position1 = 320
    else:
        pass

    if difference_array[0, position0] == 0 and thresh[0] == 0:
        position0 = 0
    else:
        pass

    if np.amin(difference_array) == np.amax(difference_array):
        if thresh[0] == 255:
            mean_position = 0
            thickness = 0
        else:
            mean_position = 0
            thickness = 320
        return mean_position, thickness
    else:
        mean_position = (position1 + position0) / 2
        mean_position = math.ceil(mean_position)
        thickness = position1 - position0
        return mean_position, thickness

def PID(mean_position):
    global kp, kd, ki, last_propotional, integral, maxi, lastState, lastPwm

    derivative = mean_position - last_propotional
    integral += mean_position
    last_propotional = mean_position

    if mean_position > 200:
        right()
        set_motor_speed(maxi, maxi)
        lastState = right
        lastPwm['left'] = maxi
        lastPwm['right'] = maxi
    elif mean_position < 100:
        left()
        set_motor_speed(maxi, maxi)
        lastState = left
        lastPwm['left'] = maxi
        lastPwm['right'] = maxi
    else:
        lastState = strai

        strai()
        duty_change = kp * mean_position + kd * derivative + ki * integral

        if duty_change > maxi:
            duty_change = maxi
        elif duty_change < (-maxi):
            duty_change = -maxi
        else:
            pass

        if duty_change > 0:
            set_motor_speed(maxi - duty_change, maxi)
            lastPwm['left'] = maxi - duty_change
            lastPwm['right'] = maxi
        else:
            set_motor_speed(maxi, maxi - math.fabs(duty_change))
            lastPwm['left'] = maxi
            lastPwm['right'] = maxi - math.fabs(duty_change)

def set_motor_speed(left_motor_speed, right_motor_speed):
    global pwmright, pwmleft
    pwmleft.ChangeDutyCycle(float(left_motor_speed))
    pwmright.ChangeDutyCycle(float(right_motor_speed))

if __name__ == '__main__':
    pass
