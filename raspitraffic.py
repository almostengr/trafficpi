#!/usr/bin/python

################################################################################
# Project: Raspi Traffic Control
# Script Usage: raspitraffic.py
# Created: 2017-04-02
# Author: Kenny Robinson, @almostengr, www.bitsecondtech.com
# Description: Core script which all the functions for controlling the lights
# are contained.
################################################################################

from time import sleep
from random import randint
import RPi.GPIO as GPIO
# import lcddriver
import random
import sys
import os
import subprocess

# DEBUGGING MODE, DISABLED=0, ENABLED=1
DEBUG=0

# LIST ALL OF THE PINS USED
pinOutList = [23, 21, 19]

# DEFINE THE GPIO NUMBERS AND VARIABLES FOR THE EASTBOUND TRAFFIC
EAST_CR = 23
EAST_CY = 21
EAST_CG = 19

# DEFINE CONSTANTS
LAMPON=GPIO.LOW
LAMPOFF=GPIO.HIGH
FLASHER_DELAY=.7

# display=lcddriver.lcd()
selection = 0
phaseflasher=0
phasenum=0


def setup():
# SET UP GPIO PINS
	GPIO.setmode(GPIO.BOARD)

	# disable GPIO warnings when not debugging
	if DEBUG == 0:
		GPIO.setwarnings(False)

	# loop through each of the pins and define it.
	# turn on all the lights once setup
	for i in pinOutList:
		debug_message("Setting up and activiating pin " + str(i))
		GPIO.setup(i, GPIO.OUT)

	debug_message("Waiting")

	sleep(1)

	# turn off all the lights
	for i in pinOutList:
		GPIO.output(i, GPIO.HIGH)
		lcd_message("Done performing setup", "")
		lcd_message("", "")

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
# print message on computer screen
	print message
	return 0


def lcd_message(line1, line2):
# Displays the message on the LCD screen and computer screen
	log_message(line1 + " | " + line2)
	return 0


def terminate():
# WHEN COMMAND TO EXIT IS GIVEN, THEN RESET EVERYTHING BACK TO DEFAULT
	log_message("Exiting")
	GPIO.cleanup()
	# display.lcd_clear()


def run_red_light_green_light():
# SEQUENCE FOR RED LIGHT GREEN LIGHT GAME.

	red_time=randint(2, 10)
	green_time=randint(0, 3)
	
	eblight(LAMPON, LAMPOFF, LAMPOFF)
	debug_message("Red Time: " + str(red_time))
	lcd_message("Red Light!", "Dont move!")
	sleep(red_time)

	eblight(LAMPOFF, LAMPOFF, LAMPON)
	debug_message("Green Time: " + str(green_time))
	lcd_message("Green Light!", "Run!")
	sleep(green_time)


def run_signal(country):
# runs the light using normal signal
	phaseflasher=0

	east_grn_time=random.randint(5, 30)
	east_yel_time=random.randint(2, 5)
	east_red_time=random.randint(5, 30)

	# red
	eblight(LAMPON, LAMPOFF, LAMPOFF)
	for ttime in range(east_red_time, 0, -1):
		lcd_message("Red", "Time Remain: " + str(ttime) + "s")
		sleep(1)

	# red-yellow for UK only
	if country == "UK":
		eblight(LAMPON, LAMPON, LAMPOFF)
		for ttime in range(east_yel_time, 0, -1):
			lcd_message("Red-Yellow", "Time Remain: " + str(ttime) + "s")
			sleep(1)

	# green
	eblight(LAMPOFF, LAMPOFF, LAMPON)
	for ttime in range(east_grn_time, 0, -1):
		lcd_message("Green", "Time Remain: " + str(ttime) + "s")
		sleep(1)

	# yellow
	eblight(LAMPOFF, LAMPON, LAMPOFF)
	for ttime in range(east_yel_time, 0, -1):
		lcd_message("Yellow", "Time Remain: " + str(ttime) + "s")
		sleep(1)

	# red
	eblight(LAMPON, LAMPOFF, LAMPOFF)
	for ttime in range(east_red_time, 0, -1):
		lcd_message("Red", "Time Remain: " + str(ttime) + "s")
		sleep(1)

	# change flasher color
	if phaseflasher == 1 or phaseflasher == 2:
		inColor = "yellow"
		lcd_message("Yellow Flasher", "")
	else:
		inColor = "red"
		lcd_message("Red Flasher", "")

	# flasher
	flashrangemax=randint(2,60)
	for i in range(1,flashrangemax):
		phaseflasher = run_flasher(inColor, phaseflasher)


def run_flasher(color, phase):
# flash the lights
	if color == "red":
		if phase == 1:
			eblight(LAMPOFF, LAMPOFF, LAMPOFF)
			lcd_message("Flashing Red", "")
			phase = 2
		else:
			eblight(LAMPON, LAMPOFF, LAMPOFF)
			lcd_message("Flashing Red Off", "")
			phase = 1

	elif color == "yellow":
		if phase == 3:
			eblight(LAMPOFF, LAMPOFF, LAMPOFF)
			lcd_message("Flashing Yellow", "")
			phase = 4
		else:
			eblight(LAMPOFF, LAMPON, LAMPOFF)
			lcd_message("Flashing Yellow Off", "")
			phase = 3

	elif color == "green":
		if phase == 7:
			eblight(LAMPOFF, LAMPOFF, LAMPOFF)
			lcd_message("Flashing Green", "")
			phase = 8
		else:
			eblight(LAMPOFF, LAMPOFF, LAMPON)
			lcd_message("Flashing Green Off", "")
			phase = 7

	sleep(FLASHER_DELAY)

	return phase


def calc_yellow_time( speed, grade ):
# CALCULATE THE AMOUNT OF YELLOW LIGHT TIME
	yel_time = 1 + ((1.47 * speed) / (2 * (10 + (0 / 100) * 32.2)))
	return yel_time


def calc_green_time():
# SET A RANDOM VALUE FOR THE GREEN TIME
	grn_time=random.randint(10, 45)
	return grn_time


def eblight(cirred, ciryel, cirgrn):
# CONTROLS THE LAMPS ON THE EASTBOUND LIGHT. DOESNT HAVE LEFT TURN
	GPIO.output(EAST_CR, cirred)
	GPIO.output(EAST_CY, ciryel)
	GPIO.output(EAST_CG, cirgrn)


def randomspeed():
# picks a random speed from the range defined below
	speed=random.randint(25,65)
	return speed


def allon(phase):
# TURNS ON THE LIGHTS BASED ON THE ARGUMENT PROVIDED
	if phase == "all":
		eblight(LAMPON, LAMPON, LAMPON)
		lcd_message("ALL LIGHTS ON", "")
	elif phase == "red":
		eblight(LAMPON, LAMPOFF, LAMPOFF)
		lcd_message("ALL REDS ON", "")
	elif phase == "yellow":
		eblight(LAMPOFF, LAMPON, LAMPOFF)
		lcd_message("ALL YELLOWS ON", "")
	elif phase == "green":
		eblight(LAMPOFF, LAMPOFF, LAMPON)
		lcd_message("ALL GREENS ON", "")
	else:
		log_message("Doing nothing")

	sleep(3)


def alloff():
# TURNS OFF ALL OF THE LIGHTS
	lcd_message("ALL LIGHTS OFF", "")
	eblight(LAMPOFF, LAMPOFF, LAMPOFF)
	sleep(3)


def lamptest():
	lcd_message("LAMP TEST", "")

	eblight(LAMPON, LAMPOFF, LAMPOFF)
	sleep(1)
	eblight(LAMPON, LAMPON, LAMPOFF)
	sleep(1)
	eblight(LAMPON, LAMPON, LAMPON)

	lcd_message("LAMP TEST", "ALL ON")
	sleep(5)

	eblight(LAMPOFF, LAMPON, LAMPON)
	sleep(1)
	eblight(LAMPOFF, LAMPOFF, LAMPON)
	sleep(1)
	eblight(LAMPOFF, LAMPOFF, LAMPOFF)

	lcd_message("LAMP TEST", "ALL OFF")
	sleep(3)


# configure everything
# setup()

while True:
	debug_message("Debug mode enabled")

	try:
		try:
			file = open("/tmp/traffic.txt", "r")
			selection = file.readline()
			file.close()

		except IOError:
			# if the file doesn't exist, then create it and give public permissions
			file = open("/tmp/traffic.txt", "w")
			subprocess.call(['chmod', '0777', '/tmp/traffic.txt'])
			file.close()

		if selection == "":
			# allon("all")
			run_signal("US")

		elif selection == "allon":
		# all lights on
			allon("all")

		elif selection == "alloff":
		# all lights off
			alloff()

		elif selection == "flashred":
		# flash red
			lcd_message("Flashing Red", "")
			phaseflasher=run_flasher("red", phaseflasher)

		elif selection == "flashyel":
		# flash yellow
			lcd_message("Flashing Yellow", "")
			phaseflasher = run_flasher("yellow", phaseflasher)

		elif selection == "flashgrn":
		# flash green
			lcd_message("Flashing Green", "")
			phaseflasher=run_flasher("green", phaseflasher)

		elif selection == "3":
		# green on
			allon("green")

		elif selection == "4":
		# yellow on
			allon("yellow")

		elif selection == "5":
		# red on
			allon("red")

		elif selection == "ustraffic":
		# US signal pattern
			run_signal("US")

		elif selection == "uktraffic":
		# UK signal pattern
			run_signal("UK")

		elif selection == "redlightgreenlight":
			run_red_light_green_light()

		elif selection == "shutdown":
		# shutdown the system
			subprocess.call(["sudo", "shutdown", "-h", "now"])

	except KeyboardInterrupt:
		terminate()

