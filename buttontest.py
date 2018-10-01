import RPi.GPIO as GPIO
from neopixel import *
import sys, time

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

def wheel(pos):
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def theaterChaseRainbow(strip, wait_ms=50):
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def rainbowCycle(strip, wait_ms=20, iterations=1):
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

try:
    while True:
        if GPIO.input(10) == GPIO.HIGH:
            #print("Button was pushed!")
            #colorAll(strip, Color(0, 90, 0))
            rainbowCycle(strip)
        else:
            colorAll(strip, Color(0, 0, 0))
except KeyboardInterrupt:
    colorAll(strip, Color(0, 0, 0))
