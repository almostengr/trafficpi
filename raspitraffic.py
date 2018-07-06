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
import lcddriver
import random
import subprocess

# DEBUGGING MODE, DISABLED=0, ENABLED=1
DEBUG=0

# LIST ALL OF THE PINS USED
PINOUTLIST=[23, 21, 19]

# DEFINE THE GPIO NUMBERS AND VARIABLES FOR THE EASTBOUND TRAFFIC
EAST_CR=23
EAST_CY=21
EAST_CG=19

# DEFINE ADDITIONAL CONSTANTS
LAMPON=GPIO.LOW
LAMPOFF=GPIO.HIGH
FLASHER_DELAY=.7

# display=lcddriver.lcd()
selection=0
phaseflasher=0
phasenum=0
run_signal_flasher="red"

def setup():
# SET UP GPIO PINS
	GPIO.setmode(GPIO.BOARD)

	# disable GPIO warnings when not debugging
	if DEBUG == 0:
		GPIO.setwarnings(False)

	# loop through each of the pins and define it.
	# turn on all the lights once setup
	for i in PINOUTLIST:
		debug_message("Setting up and activiating pin " + str(i))
		GPIO.setup(i, GPIO.OUT)

	debug_message("Waiting")
	sleep(1)

	# turn off all the lights
	for i in PINOUTLIST:
		GPIO.output(i, GPIO.HIGH)
		debug_message("Turning off pin " + str(i))

	lcd_message("Done performing setup", "")

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


def run_red_light_green_light(yellowon):
# SEQUENCE FOR RED LIGHT GREEN LIGHT GAME.
	
	# generate random values for red and green
	red_time=randint(1, 10)
	green_time=randint(1, 3)
	yellow_time=FLASHER_DELAY

	# Turn on the red light and wait
	eblight(LAMPON, LAMPOFF, LAMPOFF)
	debug_message("Red Time: " + str(red_time))
	lcd_message("Red Light!", "Dont move!")
	sleep(red_time)

	# Turn on the green light and wait
	eblight(LAMPOFF, LAMPOFF, LAMPON)
	debug_message("Green Time: " + str(green_time))
	lcd_message("Green Light!", "Run!")
	sleep(green_time)
	
	# If playing with yellow light, then turn on the yellow light
	if yellowon == 1:
		eblight(LAMPOFF, LAMPON, LAMPOFF)
		debug_message("Yellow Time: " + str(yellow_time))
		lcd_message("Yellow Light!", "Slow!")
		sleep(yellow_time)


def run_signal(country):
# runs the light using normal signal
	phaseflasher=0

	# generate random values for the lights to stay on
	east_grn_time=random.randint(5, 30)
	east_yel_time=random.randint(2, 5)
	east_red_time=random.randint(5, 30)

	# green
	eblight(LAMPOFF, LAMPOFF, LAMPON)
	for ttime in range(east_grn_time, 0, -1):
		lcd_message("Green", "Time Remain: " + str(ttime) + "s")
		sleep(1)

        # flash green if selected
        if country == "russiatraffic":
            for i in range(4, randint(5,10)):
                phaseflasher=run_flasher("green", phaseflasher)

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

	# red-yellow for UK only
	if country == "UK":
		eblight(LAMPON, LAMPON, LAMPOFF)
		for ttime in range(east_yel_time, 0, -1):
			lcd_message("Red-Yellow", "Time Remain: " + str(ttime) + "s")
			sleep(1)

def run_flasher(color, phase):
# flash the lights
	if color == "red":
		if phase == 1:
			eblight(LAMPOFF, LAMPOFF, LAMPOFF)
			lcd_message("Flashing Red Off", "")
			phase=2
		else:
			eblight(LAMPON, LAMPOFF, LAMPOFF)
			lcd_message("Flashing Red", "")
			phase=1

	elif color == "yellow":
		if phase == 3:
			eblight(LAMPOFF, LAMPOFF, LAMPOFF)
			lcd_message("Flashing Yellow Off", "")
			phase=4
		else:
			eblight(LAMPOFF, LAMPON, LAMPOFF)
			lcd_message("Flashing Yellow", "")
			phase=3

	elif color == "green":
		if phase == 7:
			eblight(LAMPOFF, LAMPOFF, LAMPOFF)
			lcd_message("Flashing Green Off", "")
			phase=8
		else:
			eblight(LAMPOFF, LAMPOFF, LAMPON)
			lcd_message("Flashing Green", "")
			phase=7
	
	elif color == "all":
		if phase == 9:
			eblight(LAMPON, LAMPON, LAMPON)
			lcd_message("Flashing All", "")
			phase=10
		else:
			eblight(LAMPOFF, LAMPOFF, LAMPOFF)
			lcd_message("Flashing All Off", "")
			phase=9

	sleep(FLASHER_DELAY)
	return phase


def calc_yellow_time(grade):
# CALCULATE THE AMOUNT OF YELLOW LIGHT TIME
        speed=randint(25,80)
	yel_time=1 + ((1.47 * speed) / (2 * (10 + (0 / 100) * 32.2)))
	return yel_time


def eblight(cirred, ciryel, cirgrn):
# CONTROLS THE LAMPS ON THE EASTBOUND LIGHT.
	GPIO.output(EAST_CR, cirred)
	GPIO.output(EAST_CY, ciryel)
	GPIO.output(EAST_CG, cirgrn)


def all_on(phase):
# TURNS ON THE LIGHTS BASED ON THE ARGUMENT PROVIDED

	# turn on all the lights
	if phase == "all":
		eblight(LAMPON, LAMPON, LAMPON)
		lcd_message("ALL LIGHTS ON", "")
	
	# turn on the red light
	elif phase == "red":
		eblight(LAMPON, LAMPOFF, LAMPOFF)
		lcd_message("ALL REDS ON", "")

	# turn on the yellow light
	elif phase == "yellow":
		eblight(LAMPOFF, LAMPON, LAMPOFF)
		lcd_message("ALL YELLOWS ON", "")

	# turn on the green light
	elif phase == "green":
		eblight(LAMPOFF, LAMPOFF, LAMPON)
		lcd_message("ALL GREENS ON", "")

	# do nothing
	else:
		log_message("Doing nothing")

	sleep(3)


def all_off():
# TURNS OFF ALL OF THE LIGHTS
	lcd_message("ALL LIGHTS OFF", "")
	eblight(LAMPOFF, LAMPOFF, LAMPOFF)
	sleep(3)


# configure everything
setup()

# loop forever
while True:
	debug_message("Debug mode enabled")

	try:
		try:
		# Read the data file
			file=open("/tmp/traffic.txt", "r")
			selection=file.readline()
			file.close()

		except IOError:
		# if the file doesn't exist, then create it and give public permissions
			file=open("/tmp/traffic.txt", "w")
			subprocess.call(['chmod', '0777', '/tmp/traffic.txt'])
			file.close()

		if selection == "ustraffic":
		# run the US traffic program
			run_signal("US")

		elif selection == "all_on":
		# all lights on
			all_on("all")

		elif selection == "redon":
		# red on
			all_on("red")
	
		elif selection == "yellowon":
		# yellow on
			all_on("yellow")

		elif selection == "greenon":
		# green on
			all_on("green")

		elif selection == "all_off":
		# all lights off
			all_off()

		elif selection == "flashred":
		# flash red
			phaseflasher=run_flasher("red", phaseflasher)

		elif selection == "flashyel":
		# flash yellow
			phaseflasher=run_flasher("yellow", phaseflasher)

		elif selection == "flashgrn":
		# flash green
			phaseflasher=run_flasher("green", phaseflasher)

		elif selection == "uktraffic":
		# UK signal pattern
			run_signal("UK")

                elif selection == "russiatraffic":
                # signal pattern with flashing green
                        run_signal("normalflashgreen")

		elif selection == "redlightgreenlight":
		# red light, green light
			run_red_light_green_light(0)

		elif selection == "redlightgreenlight2":
		# red light, green light, with yellow
			run_red_light_green_light(1)

		elif selection == "restart":
		# restart the Raspberry Pi
			subprocess.call(["sudo", "restart"])

		elif selection == "shutdown":
		# shutdown the Raspberry Pi
			subprocess.call(["sudo", "shutdown", "-h", "now"])
	
		else:
		# If nothing selected or bad value, default to failure state
			phaseflasher=run_flasher("all", phaseflasher)

	except KeyboardInterrupt:
	# perform action if Ctrl+C is pressed
		log_message("Exiting")
		all_off()
		# GPIO.clean()

