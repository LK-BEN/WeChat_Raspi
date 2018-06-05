import RPi.GPIO as GPIO
import time

def init_led(pin):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    
def open_led(pin):
    GPIO.output(pin, GPIO.HIGH)

def close_led(pin):
    GPIO.output(pin, GPIO.LOW)

if __name__ == '__main__':
    GPIO.setwarnings(False)
    init_led(18)
    while True:
        open_led(18)
        time.sleep(0.5)
        close_led(18) 
        time.sleep(0.5)
    
