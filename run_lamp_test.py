#!/usr/bin/python

################################################################################
# Project: 	Traffic Control
# Script Usage: run_lamp_test.py
# Created: 	2017-04-02
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Will turn on all the lights as well as display message on the 
#		LCD display to ensure everything is working as expected.
################################################################################

import time
import RPi.GPIO as GPIO
import lcddriver
import sys
import random

# LIST ALL OF THE PINS USED
pinOutList = [26, 19, 13, 6, 12, 16, 20, 21]

# DEFINE THE GPIO NUMBERS AND VARIABLES FOR NORTHBOUND TRAFFIC
NORTH_CR = 26
NORTH_CY = 19
NORTH_CG = 13
NORTH_LG = 20
NORTH_LY = 21

# DEFINE THE GPIO NUMBERS AND VARIABLES FOR THE EASTBOUND TRAFFIC
EAST_CR = 6
EAST_CY = 12
EAST_CG = 16

# DEBUG MODE, ENABLED=1, DISABLED=0
DEBUG=0

display=lcddriver.lcd()

def setup():
# SET UP GPIO PINS
	GPIO.setmode(GPIO.BCM)

	for i in pinOutList:
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, GPIO.HIGH)

	return 0

def light_on(pin):
# TURN ON THE LIGHT, HAS TO PROVIDE PIN NUMBER
	GPIO.output(pin, GPIO.LOW)
	debug_message("Pin " + str(pin) + " turned on")
	return 0

def light_off(pin):
# TURN OFF THE LIGHT, HAS TO PROVIDE PIN NUMBER
	GPIO.output(pin, GPIO.HIGH)
	debug_message("Pin " + str(pin) + " turned off")
	return 0

def debug_message(message):
# LOG ADDITIONAL MESSAGES TO THE SCREEN/LOG FILE WHEN TESTING
	if DEBUG == 1:
		log_message("DEBUG: " + message)

	return 0

def log_message(message):
# print message on LCD screen
	print message
	return 0

def lcd_message(line1, line2):
# Displays the message on the LCD screen
	display.lcd_clear()
	display.lcd_display_string(line1, 1)
	display.lcd_display_string(line2, 2)
	log_message(line1 + " | " + line2)
	return 0

def lamptest():
	lcd_message("LAMP TEST", "CYCLING ON")

	for i in pinOutList:
		light_on(i)	
		log_message("Pin " + str(i) + " turned on")
		time.sleep(1)

	lcd_message("LAMP TEST", "ALL ON")

	time.sleep(10)

	lcd_message("LAMP TEST", "CYCLING OFF")	

	for i in pinOutList:
		light_off(i)
		log_message("Pin " + str(i) + " turned off")
		time.sleep(1)
	
	lcd_message("LAMP TEST", "ALL OFF")
	
	time.sleep(3)
	
	display.lcd_clear()

try:
	setup()
	lamptest()

except KeyboardInterrupt:
	log_message("Exiting")
	GPIO.cleanup()
	display.lcd_clear()
