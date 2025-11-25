from data import *
import requests



class FlightSearch:
    def __init__(self):
        self.api = API_KEY
        self.secret = API_SECRET
        self.token = self._get_new_token()

    def _get_new_token(self):

        header = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        body = {
            "grant_type": "client_credentials",
            "client_id": self.api,
            "client_secret": self.secret
        }

        response = requests.post(url = TOKEN_ENDPOINT, headers = header, data = body)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']


    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        print(f"Using this token to get destination {self.token}")
        headers = {"Authorization": f"Bearer {self.token}"}
        query = {
            "keyword": city_name,
            "max": 2,
            "include": "AIRPORTS"
        }
        response = requests.get(url = IATA_ENDPOINT,
                                headers = headers,
                                params = query
                                )

        print(f"Status code: {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"Index Error: No airport for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"Key Error: No airport for {city_name}.")
            return "Not Found"

        return code
