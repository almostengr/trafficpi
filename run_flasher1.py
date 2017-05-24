#!/usr/bin/python

################################################################################
# Project:      Traffic Control
# Script Usage: run_flasher1.py
# Created:      2017-04-02
# Author:       Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:  Flash lights as if a malfunction or power outage has occurred.
# 		Lights will flash in opposite colors of run_flasher2.py.
################################################################################

import raspitraffic as rtc

try:
	rtc.setup()
	phaseflasher=1

	while True:
		phaseflasher=rtc.controlflasher(phaseflasher)
		rtc.flashsleep()
except KeyboardInterrupt:
	rtc.terminate()

