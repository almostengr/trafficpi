#!/usr/bin/python

################################################################################
# Project: 	Raspi Traffic Control
# Script Usage: poweron.py
# Created: 	2018-03-18
# Author: 	Kenny Robinson, @almostengr, www.bitsecondtech.com
# Description:	Turns on all the lights and exits. Configured to run on startup
################################################################################

import trafficcontrol as rtc

try:
	rtc.setup()
except KeyboardInterrupt:
	rtc.terminate()

