#!/usr/bin/python

################################################################################
# Project: 	Raspi Traffic Control
# Script Usage: raspitraffic.py
# Created: 	2017-04-02
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Core script which all the functions for controlling the lights
# 		are contained. 
################################################################################

from time import sleep
import RPi.GPIO as GPIO
import lcddriver
import random

# DEBUGGING MODE, DISABLED=0, ENABLED=1
DEBUG=0

# LIST ALL OF THE PINS USED
pinOutList = [37, 35, 33, 31, 29, 23, 21, 19]

# DEFINE THE GPIO NUMBERS AND VARIABLES FOR NORTHBOUND TRAFFIC
NORTH_CR = 37
NORTH_CY = 35
NORTH_CG = 33
NORTH_LG = 31
NORTH_LY = 29

# DEFINE THE GPIO NUMBERS AND VARIABLES FOR THE EASTBOUND TRAFFIC
EAST_CR = 23
EAST_CY = 21
EAST_CG = 19

# DEFINE CONSTANTS
LMPON=GPIO.LOW
LMPOFF=GPIO.HIGH
ALL_RED_TIME=5

display=lcddriver.lcd()

def setup():
# SET UP GPIO PINS
	GPIO.setmode(GPIO.BOARD)
	
	# loop through each of the pins and define it.
	# tun on all the lights once setup
	
	# log_message("Performing setup")
	lcd_message("Performing setup", "Please wait...")
	
	for i in pinOutList:
		debug_message("Setting up and activiating pin " + str(i))
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, GPIO.LOW)

	debug_message("Waiting")

	sleep(2)

	# turn off all the lights
	for i in pinOutList:
		GPIO.output(i, GPIO.HIGH)

	# log_message("Done performing setup")
	lcd_message("Done performing setup", "")
		
	return 0

def getallredtime():
# GETS THE VALUE OF THE ALL RED TIME
	return ALL_RED_TIME

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
# print message on computer screen
	print message
	return 0

def lcd_message(line1, line2):
# Displays the message on the LCD screen and computer screen
	display.lcd_clear()
	display.lcd_display_string(line1, 1)
	display.lcd_display_string(line2, 2)
	log_message(line1 + " | " + line2)
	return 0

def terminate():
# WHEN COMMAND TO EXIT IS GIVEN, THEN RESET EVERYTHING BACK TO DEFAULT
	log_message("Exiting")
        GPIO.cleanup()
        display.lcd_clear()

def controlflasher(phase):
# runs flasher SEQUENCE
	if phase == 0:
		log_message("Do nothing")
	elif phase == 1:
		nblight(LMPOFF, LMPON, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPOFF, LMPOFF)
		lcd_message("Flasher Mode", "EB OFF, NB YEL")
		phase=2
	elif phase == 2:
		nblight(LMPOFF, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		lcd_message ("Flasher Mode", "EB RED, NB OFF")
		phase=1
	else:
		log_message("Not valid flasher phase")
		phase=0
	return phase

def calc_yellow_time( speed, grade ):
# CALCULATE THE AMOUNT OF YELLOW LIGHT TIME
	# y = 1 + ((1.47 * speed) / (2 * (10 * (grade / 100) * 32.2))
	yel_time = 1 + ((1.47 * speed) / (2 * (10 + (0 / 100) * 32.2)))
	# yel_time = 1 +  644
	log_message("Yellow Time: " + str(yel_time))
	return yel_time

def calc_green_time():
# SET A RANDOM VALUE FOR THE GREEN TIME
	grn_time=random.randint(20, 45)
	log_message("Green Time: " + str(grn_time))
	return grn_time

def nblight(cirred, ciryel, cirgrn, lefyel, lefgrn):
# CONTROLS THE LAMPS ON THE NORTHBOUND LIGHT. DESIGNED TO INCLUDE LEFT TURN
	GPIO.output(NORTH_CR, cirred)
	GPIO.output(NORTH_CY, ciryel)
	GPIO.output(NORTH_CG, cirgrn)
	GPIO.output(NORTH_LY, lefyel)
	GPIO.output(NORTH_LG, lefgrn)

def eblight(cirred, ciryel, cirgrn):
# CONTROLS THE LAMPS ON THE EASTBOUND LIGHT. DOESNT HAVE LEFT TURN
	GPIO.output(EAST_CR, cirred)
	GPIO.output(EAST_CY, ciryel)
	GPIO.output(EAST_CG, cirgrn)

def controlring1uk(phase):
# RUN NORMAL SEQUENCE WITH UK PHASING

# phase 0 - do nothing
# phase 1 - nb cr cy, eb cr
# phase 2 - nb cg, eb cr
# phase 3 - nb cy, eb cr
# phase 4 - nb cr, eb cr cy
# phase 5 - nb cr, eb cg
# phase 6 - nb cr, eb cy
	
	debug_message("incoming phase: " + str(phase))
	
	if phase == 0:
		log_message("Do nothing")
	elif phase == 1:
		nblight(LMPON, LMPON, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		phase = 2
	elif phase == 2:
		nblight(LMPOFF, LMPOFF, LMPON, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		phase=3
	elif phase == 3:
		nblight(LMPOFF, LMPON, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		phase = 4
	elif phase == 4:
		nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPON, LMPON, LMPOFF)
		phase = 5
	elif phase == 5:
		nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPOFF, LMPON)
		phase = 6
	elif phase == 6:
		nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPON, LMPOFF)
		phase = 1 
	else:
		phase=1
	
	debug_message("outgoing phase " + str(phase))
	return phase

def controlring1(phase):
# RUN NORMAL SEQUENCE FOR NORTHBOUND AND EASTBOUND LIGHT

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
		log_message("NB RED -- EB RED")
		nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		phase = 2
	elif phase == 2:
		log_message("NB GRN -- EB RED")
		nblight(LMPOFF, LMPOFF, LMPON, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		phase = 3
	elif phase == 3:
		nblight(LMPOFF, LMPON, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		phase = 4 
		log_message("NB YEL -- EB RED")
	elif phase == 4:
		nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		phase = 5
		log_message("NB RED -- EB RED")
	elif phase == 5:
		nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPOFF, LMPON)
		phase = 6 
		log_message("NB RED -- EB GRN")
	elif phase == 6:
		nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPON, LMPOFF)
		phase = 1 
		log_message("NB RED -- EB YEL")
	else:
		phase = 1

	debug_message("Outgoing phase: " + str(phase))
	return phase

def controlring1eb(phase):
# RUN NORMAL SEQUENCE FOR EASTBOUND LIGHT ONLY

# phase 0 - do nothing
# phase 1 - eb cr
# phase 2 - eb cg
# phase 3 - eb cy

	debug_message("Incoming phase: " + str(phase))

	if phase == 0:	
		# do nothing
		log_message("Doing nothing")
	elif phase == 1:
		# red on
		eblight(LMPON, LMPOFF, LMPOFF)
		phase = 2
	elif phase == 2:
		# green on
		eblight(LMPOFF, LMPOFF, LMPON)
		phase = 3
	elif phase == 3:
		# yellow on
		eblight(LMPOFF, LMPON, LMPOFF)
		phase = 1
	else:
		phase = 1

	debug_message("Outgoing phase: " + str(phase))
	return phase

def randomspeed():
	speed=random.randint(25,50)
	return speed

def allon():
# TURNS ON ALL OF THE LIGHTS
	lcd_message("ALL LIGHTS ON", "")
	for i in pinOutList:
		light_on(i)
	sleep(3)
	display.lcd_clear()

def alloff():
# TURNS OFF ALL OF THE LIGHTS
	lcd_message("ALL LIGHTS OFF", "")
	for i in pinOutList:
		light_off(i)
	sleep(3)
	display.lcd_clear()

def lamptest():
	lcd_message("LAMP TEST", "")

	for i in pinOutList: 	
		light_on(i)
		lcd_message("LAMP TEST", "Pin " + str(i) + " on")
		sleep(1)

	lcd_message("LAMP TEST", "ALL ON")
	sleep(10)

	for i in pinOutList:
		light_off(i)
		lcd_message("LAMP TEST", "Pin " + str(i) + " off")
		sleep(1)

	lcd_message("LAMP TEST", "ALL OFF")
	sleep(3)
	display.lcd_clear()

