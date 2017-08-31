# Raspberry-GPIO-Webservice
A simple REST-webservice to control the GPIO pins of the pi 

Realized with python and flask

To active channel: http://hostname:5000/gpio/<channel>/on

To deactive channel: http://hostname:5000/gpio/<channel>/off

To clear all and clean up: http://hostname:5000/gpio/clear
