#!/bin/python
# Simple script for shutting down the raspberry Pi at the press of a button.
# by Inderpreet Singh

import RPi.GPIO as GPIO
import time
import os
import sys

# Set this to the GPIO channel.
# Channel 3 also works as a startup button.
# Unfortunately, channel 3 is not available if using an I2C device.
shutdown_channel = 23

# Blink an LED on this channel.
blink_channel = 20
blink_on = True

# Use the Broadcom SOC Pin numbers
GPIO.setmode(GPIO.BCM)

# Setup the Shutdown Pin with Internal pullups enabled and PIN in reading mode.
GPIO.setup(shutdown_channel, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Setup the LED channel.
GPIO.setup(blink_channel, GPIO.OUT)

# Our function on what to do when the button is pressed
def Shutdown(channel):
    print "Shutting down"
    sys.stdout.flush()

    GPIO.output(blink_channel, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(blink_channel, GPIO.LOW)
    time.sleep(.5)
    GPIO.output(blink_channel, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(blink_channel, GPIO.LOW)
    time.sleep(.5)
    GPIO.output(blink_channel, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(blink_channel, GPIO.LOW)

    os.system("sudo shutdown -h now")

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(shutdown_channel, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)

# Now wait!
while 1:
    if blink_on:
      GPIO.output(blink_channel, GPIO.HIGH)
      blink_on = False
    else:
      GPIO.output(blink_channel, GPIO.LOW)
      blink_on = True

    time.sleep(1)
