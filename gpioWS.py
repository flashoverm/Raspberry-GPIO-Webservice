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
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4, GPIO.OUT, initial=False)
	GPIO.setup(17, GPIO.OUT, initial=False)
	GPIO.setup(18, GPIO.OUT, initial=False)
	GPIO.setup(21, GPIO.OUT, initial=False)
	GPIO.setup(22, GPIO.OUT, initial=False)
	GPIO.setup(23, GPIO.OUT, initial=False)
	GPIO.setup(24, GPIO.OUT, initial=False)
	GPIO.setup(10, GPIO.OUT, initial=False)
	GPIO.setup(9, GPIO.OUT, initial=False)
	GPIO.setup(25, GPIO.OUT, initial=False)
	GPIO.setup(11, GPIO.OUT, initial=False)
	GPIO.setup(8, GPIO.OUT, initial=False)
	GPIO.setup(7, GPIO.OUT, initial=False)
	GPIO.cleanup()
	return 'GPIO channels cleared'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

