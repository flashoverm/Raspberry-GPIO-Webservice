# Raspberry-GPIO-Webservice
A simple REST-webservice to control the GPIO pins of the pi 

Realized with python and flask

To activate channel: http://hostname:5000/gpio/[channel]/on

To deactivate channel: http://hostname:5000/gpio/[channel]/off

To clear all channels and clean up: http://hostname:5000/gpio/clear
