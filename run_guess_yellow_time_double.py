#!/usr/bin/python

################################################################################
# Project: 	Traffic Control
# Script Usage: guess_yellow_time.py
# Created: 	2017-04-02
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Goal is to guess the amount of time that the traffic light will
# 		yellow for before it turns yellow. The script will provide a
# 		a random speed. Then using the yellow light formula, students
#		are to calculate the amount of time that the light will be for
#		before the light changes. Speed is given when the light turns 
#		green and countdown is started.
################################################################################

import time
import RPi.GPIO as GPIO
import lcddriver
import sys
import random

# LIST ALL OF THE PINS USED
pinOutList = [26, 19, 13, 6, 12, 16, 20, 21]
# pinInList = [4]

# DEFINE THE GPIO NUMBERS AND VARIABLES FOR NORTHBOUND TRAFFIC
NORTH_CR = 26
NORTH_CY = 19
NORTH_CG = 13
NORTH_LG = 20
NORTH_LY = 21
NORTH_SPEEDLIMIT = 45
NORTH_YEL_TIME = 0
NORTH_GRN_TIME = 0

# DEFINE THE GPIO NUMBERS AND VARIABLES FOR THE EASTBOUND TRAFFIC
EAST_CR = 6
EAST_CY = 12
EAST_CG = 16
EAST_SPEEDLIMIT = 25
EAST_YEL_TIME = 0
EAST_GRN_TIME = 0

# DEBUG MODE, ENABLED=1, DISABLED=0
DEBUG=0

# SET THE VALUE OF OTHER MISC VARIABLES
if DEBUG == 1:
	ALL_RED_TIME=5
else:
	ALL_RED_TIME=10

# SET INITIAL VALUE FOR THE PHASES
phasering1 = 0
phaseflasher = 0

display=lcddriver.lcd()


def setup():
# SET UP GPIO PINS
	GPIO.setmode(GPIO.BCM)

	for i in pinOutList:
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, GPIO.HIGH)

	return 0

def calc_yellow_time( speed, grade ):
# CALCULATE THE AMOUNT OF YELLOW LIGHT TIME
	# y = 1 + ((1.47 * speed) / (2 * (10 * (grade / 100) * 32.2))
	yel_time = 1 + ((1.47 * speed) / (2 * (10 + (0 / 100) * 32.2)))
	log_message("Yellow Time: " + str(yel_time))
	return yel_time

def calc_green_time():
# SET A RANDOM VALUE FOR THE GREEN TIME
	grn_time=random.randint(15, 35)

	log_message("Green Time: " + str(grn_time))
	return grn_time

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

def controlflasher( phase ):
# runs flasher SEQUENCE
	if phase == 0:
		log_message("Do nothing")
	elif phase == 1:
		# lcd_message("EB YEL -- NB OFF", "MODE: Flasher")
		lcd_message("EB YEL -- NB OFF", "")
		light_on(EAST_CY)
		light_off(NORTH_CR)
		# log_message("EB Yellow on")
		# log_message("NB red off")
		phase=2
	elif phase == 2:
		light_on(NORTH_CR)
		light_off(EAST_CY)
		# lcd_message("EB OFF -- NB RED", "MODE: Flasher")
		lcd_message ("EB OFF -- NB RED", "")
		# log_message("EB yellow off")
		# log_message("NB red on")	
		phase=1
	else:
		log_message("Not valid flasher phase")
		phase=0
	return phase


def failsafe(phaseflash, phasering1 ):
# MAKE SURE THAT THE TRAFFIC LIGHT DOES GO INTO AN INVALID STATE THAT WOULD CAUSE AN ACCIDENT
	if (phaseflash == 0 and phasering1 == 0):
		# ENABLE THE FLASHER IF SOMETHING GOES WRONG
		failsafe=1
		lcd_message ("Fail safe occurred.")

	return failsafe

def controlring1( phase ):
# RUN NORMAL RUN SEQUENCE

# phase 0 - do nothing
# phase 1 - nb cr, eb cr
# Phase 2 - nb cg, eb cr
# phase 3 - nb cy, eb cr
# phase 4 - nb cr, eb cr
# phase 5 - nb cr, eb cg
# phase 6 - nb cr, eb cy
	debug_message("incoming phase: " + str(phase))

	if phase == 0:
		log_message("Doing nothing")
	elif phase == 1:
		light_on(NORTH_CR)
		light_off(NORTH_CY)
		light_off(NORTH_CG)
		light_off(NORTH_LG)
		light_off(NORTH_LY)
		light_on(EAST_CR)
		light_off(EAST_CY)
		light_off(EAST_CG)

		phase = 2
		log_message("NB RED -- EB RED")
		# time.sleep(ALL_RED_TIME)
	elif phase == 2:
		light_off(NORTH_CR)
		light_off(NORTH_CY)
		light_on(NORTH_CG)
		light_on(EAST_CR)
		light_off(EAST_CY)
		light_off(EAST_CG)

		phase = 3
		log_message("NB GRN -- EB RED")
	elif phase == 3:
		light_off(NORTH_CR)
		light_on(NORTH_CY)
		light_off(NORTH_CG)
		light_on(EAST_CR)
		light_off(EAST_CY)
		light_off(EAST_CG)

		phase = 4 
		log_message("NB YEL -- EB RED")
	elif phase == 4:
		light_on(NORTH_CR)
		light_off(NORTH_CY)
		light_off(NORTH_CG)
		light_on(EAST_CR)
		light_off(EAST_CY)
		light_off(EAST_CG)
		
		phase = 5
		log_message("NB RED -- EB RED")
		# time.sleep(ALL_RED_TIME)
	elif phase == 5:
		light_on(NORTH_CR)
		light_off(NORTH_CY)
		light_off(NORTH_CG)
		light_off(EAST_CR)
		light_off(EAST_CY)
		light_on(EAST_CG)
		
		phase = 6 
		log_message("NB RED -- EB GRN")
	elif phase == 6:
		light_on(NORTH_CR)
		light_off(NORTH_CY)
		light_off(NORTH_CG)
		light_off(EAST_CR)
		light_on(EAST_CY)
		light_off(EAST_CG)

		phase = 1 
		log_message("NB RED -- EB YEL")
	else:
		phase = 1

	debug_message("Outgoing phase: " + str(phase))
	return phase

def controlring2():
	return 0

def randomspeed():
	speed=random.randint(25,50)
	return speed

def lamptest():
	lcd_message("LAMP TEST", "IN PROGRESS")

	for i in pinOutList:
		light_on(i)	
		time.sleep(1)

	time.sleep(10)

	for i in pinOutList:
		light_off(i)
		time.sleep(1)
	
	display.lcd_clear()

try:
	setup()
	
	debug_message("Debug mode enabled")

	phaseflasher=0
	phasering1=1

	while True:
		# lcd_message("All Red Delay", "")

		debug_message("Turning all red")

		phasering1=controlring1(phasering1)

		for x in range(ALL_RED_TIME, 0, -1):	
			lcd_message("All Red Delay", "Starting in " + str(x) + "s")
			time.sleep(1)

		## BOUNDARY

		NORTH_SPEEDLIMIT=randomspeed()
		EAST_SPEEDLIMIT=randomspeed()

		debug_message("Turning north green")
	
		NORTH_GRN_TIME=calc_green_time()

		phasering1=controlring1(phasering1)

		for x in range(NORTH_GRN_TIME, 0, -1):
			lcd_message("Speed Limit: " + str(NORTH_SPEEDLIMIT), "Time Remain: " + str(x) + "s")
			time.sleep(1)
		# time.sleep(NORTH_GRN_TIME)

		debug_message("Turning north yellow")

		NORTH_YEL_TIME=calc_yellow_time(NORTH_SPEEDLIMIT, 0)

		phasering1=controlring1(phasering1)

		lcd_message("Yellow Time: ", str(NORTH_YEL_TIME) + " seconds")
		time.sleep(NORTH_YEL_TIME)

		debug_message("turning all red")

		phasering1=controlring1(phasering1)

		# lcd_message("All red delay", "")
		for x in range(ALL_RED_TIME, 0, -1):
			lcd_message("All Red Delay", "Starting in " + str(x) + "s")
			time.sleep(1)


		## BOUNDARY

		EAST_GRN_TIME=calc_green_time()

		debug_message("Turning east green")

		phasering1=controlring1(phasering1)

		for x in range(EAST_GRN_TIME, 0, -1):
			lcd_message("Speed Limit: " + str(EAST_SPEEDLIMIT), "Time Remain: " + str(x) + "s")
			time.sleep(1)

		debug_message("Turning east yellow")

		EAST_YEL_TIME=calc_yellow_time(EAST_SPEEDLIMIT, 0)

		phasering1=controlring1(phasering1)

		lcd_message("Yellow Time: ", str(EAST_YEL_TIME) + " seconds")
		
		time.sleep(EAST_YEL_TIME)

except KeyboardInterrupt:
	log_message("Exiting")
	GPIO.cleanup()
	display.lcd_clear()
