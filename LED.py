import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
LEDs={'Red':36,'Green':38,'Blue':40,'red':36,'green':38,'blue':40,'undefined':40,'Undefined':40}
#LEDRed=36
#LEDGreen=38
#LEDBlue=40
colororder=[] #Stores color order of color markers
GPIO.setup(LEDs['Red'],GPIO.OUT)
GPIO.setup(LEDs['Blue'],GPIO.OUT)
GPIO.setup(LEDs['Green'],GPIO.OUT)

GPIO.output(LEDs['Red'],GPIO.LOW)
GPIO.output(LEDs['Green'],GPIO.LOW)
GPIO.output(LEDs['Blue'],GPIO.LOW)
def addColor(color):
	colororder.append(color)
	
def blinkLEDFinal():
	global LEDs
	global colororder
	i = colororder[0]
	for i in colororder:
	#	if i==1:
#			GPIO.output(LEDRed,HIGH)
#		elif i==2:
#			GPIO.output(LEDGreen,HIGH)
#		elif i==3:
#			GPIO.output(LEDBlue,HIGH)
#		time.sleep(1)
#		GPIO.output(LEDRed,LOW)
#		GPIO.output(LEDGreen,LOW)
#		GPIO.output(LEDBlue,LOW)
		GPIO.output(LEDs[i],GPIO.HIGH)
		time.sleep(1.0)
		GPIO.output(LEDs[i],GPIO.LOW)
		time.sleep(1.0)

	
def blinkLED(color,number):
	#if color=='Blue':
	#	LED=LEDBlue

	#elif color='Green':
	#	LED=LEDGreen

	#else:
	#	LED=LEDRed
	global LEDs
	for i in range(number):
		GPIO.output(LEDs[color],GPIO.HIGH)
		print color,'LED on'
		time.sleep(1.0)
		GPIO.output(LEDs[color],GPIO.LOW)
		print color,'LED on'
		time.sleep(1.0)
