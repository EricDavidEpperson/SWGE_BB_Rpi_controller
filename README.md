# SWGE_BB_Rpi_controller
Python script to use bluetooth on Rpi 3/4 or Zero W to control a Disney SW:GE BB-8 droid

I created this script to controll a Disney Star Wars Galaxy's Edge BB-8 droid. I've tested using a Raspberry Pi 4 running Raspbian OS, with an attached Sparkfun Qwiic Joystick. This script runs as Python3. The first line can be modified to run with Python2, and it should work, but it's untested.

The Sparkfun Qwiic components have their own firmware that designates their IIC (I2C) address on the RPi bus. This Joystick has its own Analog to Digital Converter (ADC), so its a straighforward plug and play solution. There are shims, hats, and cables available for many hook up options. https://www.sparkfun.com/products/15168

Basic Functions provided:
 - 3-speed forward and backward throttle
 - turning left or right in forwards and reverse motion
 - head spins left or right

This should also work with Disney SWGE R droids, but there is no code to control their independent head swivel. You'll only have the first 2 basic functions as listed above, along with the body itself spinning in place. It will be necessary to use another control input to properly enable that functionality (It's possible to use the BB head spin to control the R head spin, but you'd lose at least some functionality of the whole body being able to spin). I also do not have a R droid to test/play with.

You'll need to do the following steps to start using this script:
1. Make sure the dependent linux libraries are installed:
     > sudo apt-get install python3-pip libglib2.0-dev i2c-tools
2. Install the necessary Python dependencies (bluepy sends bluetooth commands to the droid, smbus2 reads the joystick)
     > sudo pip3 install bluepy smbus2
3. Enable I2C:
	   1.Run sudo raspi-config.
	   2.Use the down arrow to select "5 Interfacing Options"
	   3.Arrow down to P5 I2C.
	   4.Select yes when it asks you to enable I2C
	   5.Select OK and then Finish
4. Once you copy this script to your Rpi, make sure to modify the permissions so it will run
     > sudo chmod +755 controller.py
     
You'll need to find your droid's Bluetooth address and edit the script on line 29, replacing the value in the quotion marks. Maybe in a later update, I'll create something to select from available droids.

Speaking of updates, the Joystick has a button function when you push it, and I'll probably add in a "speak" function soon.

My ultimate goal is to create a controller with the Joystick, Rpi, battery, and power management, in a custom case. Details will be added as this progresses.
