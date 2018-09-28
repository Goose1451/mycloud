import requests, json, sys
import time

i = 0

while True:
    i = i + 1
    r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20item.forecast%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text=%22portland,%20or%22)&format=json')
    #print(r.text)
    weather = json.loads(r.text)
    todayCode = (weather['query']['results']['channel'][0]['item']['forecast']['code'])
    todayText = (weather['query']['results']['channel'][0]['item']['forecast']['text'])
    todayDate = (weather['query']['created'])
    print("(" + str(i) + ") Today's code is " + todayCode + " = " + todayText + ". Created on " + todayDate)
    time.sleep(60)
    #print("Arguments are: " + str(sys.argv))
