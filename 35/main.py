import requests

from info import API_KEY

weather = "https://api.openweathermap.org/data/2.5/forecast"


weather_params = {
    "appid": API_KEY,
    "lat" : 48.172375,
    "lon" : 16.286915,
    "cnt" : 4

}

response = requests.get(weather,params=weather_params)

x = response.json()
will_rain = False
for hour in x["list"]:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) >= 700:
        will_rain = True

if will_rain:
    print("Raining")