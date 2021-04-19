import requests
import os
from twilio.rest import Client

API_KEY = os.environ["OWM_API_KEY"]
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
twilio_number = os.environ["TWILIO_NUMBER"]
test_number = os.environ["HOME_NUMBER"]

weather_params = {
    "lat": 52.520008,
    "lon": 13.404954,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="The rain is coming! ☔️", from_=twilio_number, to=test_number
    )

    print(message.status)