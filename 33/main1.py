import requests
from datetime import datetime


HOME_LAT = 48.172376
HOME_LONG = 16.286915

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

latitude = response.json()["iss_position"]["latitude"]
longitude = response.json()["iss_position"]["longitude"]

parameters = {
    "lat" : latitude,
    "lng" : longitude,
    "formatted" : 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()
x= int(data["results"]["sunrise"].split("T")[1].split(":")[0])
y = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now().hour

if x < time_now > y:
    print("Yes")
else:
    print("No")


# if (HOME_LAT + 5) > float(latitude) > (HOME_LAT - 5) and (HOME_LONG + 5) > float(longitude) > (HOME_LONG - 5) and x > time_now > y:
#     print("YES")
# else:
#     print("NO")

print(latitude, longitude)
print(x)
print(y)
print(time_now)