from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

@app.route('/')
def index():
    return 'Service running'

@app.route('/gpio/<int:channel>/on')
def gpioChannelOn(channel):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(channel, GPIO.OUT, initial=False)
	GPIO.output(channel, True)
	return 'GPIO channel %d on' % channel

@app.route('/gpio/<int:channel>/off')
def gpioChannelOff(channel):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(channel, GPIO.OUT, initial=False)
        GPIO.output(channel, False)
        return 'GPIO channel %d off' % channel

@app.route('/gpio/clear')
def gpioClear():
	GPIO.cleanup()
	return 'GPIO channels cleared'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

