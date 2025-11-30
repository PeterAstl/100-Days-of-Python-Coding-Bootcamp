import requests
from bs4 import BeautifulSoup
from data import *

response = requests.get(URL, headers={"User-Agent": USER_AGENT, "Accept-Language": LANGUAGE})

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(class_="a-offscreen")

number_price = price.text
print(number_price)
number_price = number_price.replace("€", "")
number_price = number_price.replace(",",".")
number_price = float(number_price)


if number_price < 100:
    print("Buy Now!")