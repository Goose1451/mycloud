import RPi.GPIO as GPIO
from neopixel import *

LED_COUNT    =20
LED_PIN      =18
LED_FREQ_HZ  =800000
LED_DMA      =10
LED_INVERT   =False

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
strip.begin()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def colorAll(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

while True:
    if GPIO.input(10) == GPIO.HIGH:
        #print("Button was pushed!")
        colorAll(strip, Color(0, 90, 0))
    else:
        colorAll(strip, Color(0, 0, 0))
