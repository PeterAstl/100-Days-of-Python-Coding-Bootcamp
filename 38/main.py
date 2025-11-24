from time import process_time_ns

from data import *
import requests
from datetime import datetime

datetime = datetime.now()
base_url = "https://app.100daysofpython.dev"
sheet_url = "https://api.sheety.co/078f579474dcb12afdb005474b220ac8/myWorkout/workouts"
info = input("What did you do today?")


header = {
    "x-app-key": APP_KEY,
    "x-app-id": APP_ID,
    "Content-Type": "application/json"
}

data = {
    "query" : info
}

response = requests.post(url= f"{base_url}/v1/nutrition/natural/exercise",json=data, headers= header)

result = response.json()
print(response.text)

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": datetime.strftime("%d/%m/%Y"),
            "time": datetime.strftime("%H:%M"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


header_sheet = {
    "Authorization": f"Bearer {TOKEN}",
}

print(sheet_inputs)

response_sheet = requests.post(sheet_url, json=sheet_inputs, headers=header_sheet)

print(response_sheet.text)