import json, requests, time

from neopixel import *

LED_COUNT    = 20
LED_PIN      = 18
LED_FREQ_HZ  = 800000
LED_DMA      = 5
LED_INVERT   = False

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
strip.begin()

def colorAll(strip, color):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
        strip.show()

def blueFlicker():
    colorAll(strip, Color(0, 0, 90))
    time.sleep(.25)
    colorAll(strip, Color(0, 0, 70))
    time.sleep(.25)
    colorAll(strip, Color(0, 0, 50))
    time.sleep(.25)
    colorAll(strip, Color(0, 0, 30))
    time.sleep(.25)
    colorAll(strip, Color(0, 0, 50))
    time.sleep(.25)
    colorAll(strip, Color(0, 0, 70))
    time.sleep(.25)

t = 0

def getWeather():
    r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20item.forecast%20from%20weather.forecast%20 \
                     where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text=%22portland,%20or%22)&format=json')
    weather = json.loads(r.text)
    global todayCode
    todayCode = (weather['query']['results']['channel'][0]['item']['forecast']['code'])

getWeather()
timer = time.time()

while True:
    t = t + 1
    if time.time() - timer > 60:
        getWeather()
        timer = time.time()
    print("(" + str(t) + ") Today's code is " + todayCode)
    if todayCode == "32":
        blueFlicker()
        print("today was 32")
    else:
        blueFlicker()
        print("today is not 32")
