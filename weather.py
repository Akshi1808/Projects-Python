import requests
import json
import os

city = input("Enter the city name: ")

url = f"http://api.weatherapi.com/v1/current.json?key=ef201c45e78b486495c132235241804&q={city}"

r = requests.get(url)
print(r.text)
print(type(r.text))
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

os.system(f"echo 'The current weather in {city} is {w} degrees' ")