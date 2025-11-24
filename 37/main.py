from multiprocessing.managers import Token

import requests
from data import *
from datetime import datetime


pixela_endpoint = "https://pixe.la/v1/users"

# https:/pixe.la/v1/users/pedaa/graphs/graph1.html

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "Bouldering",
#     "unit": "Hours",
#     "type": "int",
#     "color": "sora",
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_info = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

datetime = datetime.now()


body = {
    "date": datetime.strftime("%Y%m%d"),
    "quantity": "3",
}


response = requests.post(url= graph_info, json=body, headers=headers)
print(response.text)