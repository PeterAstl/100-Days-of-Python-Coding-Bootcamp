import requests
from data import *
from flight_search import *


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.token = TOKEN
        self.url = URL
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.url, headers=self.token)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }
            response = requests.put(
                url=f"{self.url}/{city["id"]}",
                headers=self.token,
                json=new_data
            )
            print(response.text)