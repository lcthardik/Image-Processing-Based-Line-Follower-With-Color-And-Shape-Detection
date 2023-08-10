import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
LEDs = {'Red': 36, 'Green': 38, 'Blue': 40, 'red': 36, 'green': 38, 'blue': 40, 'undefined': 40, 'Undefined': 40}
colororder = []
GPIO.setup(LEDs['Red'], GPIO.OUT)
GPIO.setup(LEDs['Blue'], GPIO.OUT)
GPIO.setup(LEDs['Green'], GPIO.OUT)
GPIO.output(LEDs['Red'], GPIO.LOW)
GPIO.output(LEDs['Green'], GPIO.LOW)
GPIO.output(LEDs['Blue'], GPIO.LOW)

def addColor(color):
    colororder.append(color)

def blinkLEDFinal():
    global LEDs
    global colororder
    for i in colororder:
        GPIO.output(LEDs[i], GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(LEDs[i], GPIO.LOW)
        time.sleep(1.0)

def blinkLED(color, number):
    global LEDs
    for i in range(number):
        GPIO.output(LEDs[color], GPIO.HIGH)
        print(color, 'LED on')
        time.sleep(1.0)
        GPIO.output(LEDs[color], GPIO.LOW)
        print(color, 'LED Off')
        time.sleep(1.0)
