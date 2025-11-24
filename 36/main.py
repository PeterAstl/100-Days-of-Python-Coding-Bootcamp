STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

import requests
from data import *


data_params = {
    "apikey": API_KEY,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,

}


response = requests.get(STOCK_ENDPOINT, params = data_params)
data = response.json()["Time Series (Daily)"]

list_data = [value for key,value in data.items()]
yesterday = list_data[0]
yesterday_data = yesterday["4. close"]

print(yesterday_data)


vor_gestern = list_data[1]
vor_gestern_data = vor_gestern["4. close"]
print(vor_gestern_data)


difference = (float(yesterday_data) - float(vor_gestern_data))*-1
print(difference)


diff_percent= difference/float(yesterday_data)*100
print(diff_percent)

if diff_percent > 1:
    new_params = {
        "apikey": API_KEY2,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=new_params)
    articles = news_response.json()["articles"]

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    three_articles = articles[:3]
    print(three_articles)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 



    x = [f"Headline: {article['title']}. \nBrief: {article ['description']}" for article in three_articles]
    print(x)


