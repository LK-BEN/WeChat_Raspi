import RPi.GPIO as GPIO
import dht114
import time
import datetime


def init_dht():
    
    # initialize GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
def read_dht():
    # read data using pin 14
    instance = dht114.DHT11(pin=14)
    result = instance.read()
    print "Read data"
    result = instance.read()
    if result.is_valid():
        print "Last valid input: " + str(datetime.datetime.now())
        print "Temperature: %d C" %result.temperature
        print"Humidity: %d %%" % result.humidity
    return result

if __name__ == '__main__':
        init_dht()
        result = read_dht()
        print "Last valid input: " + str(datetime.datetime.now())
        print "Temperature: %d C" %result.temperature
        print"Humidity: %d %%" % result.humidity
        time.sleep(1)
