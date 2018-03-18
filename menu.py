#!/usr/bin/python

################################################################################
# Project: Raspi Traffic Control
#
# Script Usage: menu.py
#
# Created: 2018-03-18
# 
# Author: Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
#
# Description: Main menu for use with command line / ssh interface
################################################################################

import trafficcontrol as rtc
import os

selection = 0

def mainmenu():
# MAIN MENU FOR THE PROGRAM
    os.system('clear')

    rtc.og_message("Main Menu")
    rtc.og_message("====================")
    rtc.og_message("1) All Lights On")
    rtc.og_message("2) All Lights Off")
    rtc.og_message("3) Green On")
    rtc.og_message("4) Yellow On")
    rtc.og_message("5) Red On")
    rtc.og_message("6) Flash Red")
    rtc.og_message("8) Flash Green")
    rtc.og_message("9) Flash Yellow")
    rtc.og_message("20) US Signal")
    rtc.og_message("21) UK Signal")
    rtc.og_message("Q) Exit")
    rtc.og_message("")
    rtc.og_message("Use Ctrl+C to exit running command.")

    selection = raw_input(">> ")

    return selection

# while (selection != "Q"):
while (selection != "Q" or selection != "q"):
    try:
        selection = 0
        selection = mainmenu()

        rtc.ebug_message("Debug mode enabled")

	# perform setup if not exiting
	if selection != "q" or selection != "Q":
	    rtc.etup()

        if selection == "1":
        # all lights on
            rtc.allon("all")

        elif selection == "2":
        # all lights off
            rtc.lloff()

        elif selection == "6":
        # flash red
            phaseflasher=1
            while True:
                rtc.cd_message("Flashing Red", "")
                phaseflasher=rtc.ontrolflasher(phaseflasher)
                sleep(FLASHER_DELAY)

        elif selection == "7":
        # flash yellow
            phaseflasher=9
            while True:
                rtc.cd_message("Flashing Yellow", "")
                phaseflasher=rtc.ontrolflasher(phaseflasher)
                sleep(FLASHER_DELAY)

        elif selection == "8":
        # flash green
            phasenum=7
            while True:
                rtc.cd_message("Flashing Green", "")
                phasenum=rtc.ontrolflasher(phasenum)
                sleep(FLASHER_DELAY)

        elif selection == "3":
        # green on
            rtc.llon("green")

        elif selection == "4":
        # yellow on
            rtc.llon("yellow")

        elif selection == "5":
        # red on
            rtc.llon("red")

        elif selection == "9":
	# flash yellow
            phasenum=5
            while True:
                phasenum=rtc.ontrolflasher(phasenum)
                sleep(FLASHER_DELAY)

        elif selection == "20":
        # US signal pattern
            rtc.un_signal("US")

        elif selection == "21":
        # UK signal pattern
            rtc.un_signal("UK")

        elif selection == "Q" or selection == "q":
        # exit the script
            sys.exit()

        else:
        # display.error and help message
            rtc.og_message("Invalid selection, try again.")

    except KeyboardInterrupt:
        rtc.erminate()

