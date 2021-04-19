import requests
from twilio.rest import Client
from decouple import config

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHAV_ENDPOINT = "https://www.alphavantage.co/query?"
ALPHAV_API_KEY = config("ALPHAV_API_KEY")
ALPHAV_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": ALPHAV_API_KEY,
}

alphav_request = requests.get(ALPHAV_ENDPOINT, params=ALPHAV_PARAMS)
alphav_request.raise_for_status()
alphav_response = alphav_request.json()["Time Series (Daily)"]
alphav_data = [value for (key, value) in alphav_response.items()]

yesterday_closing_price = alphav_data[0]["4. close"]
day_before_yesterday_closing_price = alphav_data[1]["4. close"]

stock_fluctuation = float(yesterday_closing_price) - float(
    day_before_yesterday_closing_price
)
stock_percentage = round((stock_fluctuation - float(yesterday_closing_price)) / 100)

if stock_percentage > 0:
    fluctuation_symbol = "🔺"
elif stock_fluctuation == 0:
    fluctuation_symbol = "🔴"
else:
    fluctuation_symbol = "🔻"

NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything?"
NEWS_API_KEY = config("NEWS_API_KEY")

NEWS_API_PARAMS = {
    "q": COMPANY_NAME,
    "sortBy": "publishedAt",
    "apiKey": NEWS_API_KEY,
}

news_api_request = requests.get(NEWS_API_ENDPOINT, params=NEWS_API_PARAMS)
news_api_request.raise_for_status()
news_api_response = news_api_request.json()
recent_articles = news_api_response["articles"][:3]

account_sid = config("ACCOUNT_SID")
auth_token = config("AUTH_TOKEN")
client = Client(account_sid, auth_token)
twilio_num = config("TWILIO_NUM")
destination_num = config("DESTINATION_NUM")

for i in range(0, 3):
    headline = recent_articles[i]["title"]
    brief = recent_articles[i]["description"]

    message = client.messages.create(
        body=f"{STOCK}: {fluctuation_symbol}{stock_percentage}%\nHeadline: {headline}\nBrief: {brief}",
        from_=twilio_num,
        to=destination_num,
    )
