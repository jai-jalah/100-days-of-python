import requests
from datetime import datetime
import smtplib
import time
from decouple import config

MY_EMAIL = config("MY_EMAIL")
MY_PASSWORD = config("MY_PASSWORD")
MY_LAT = 51.507351
MY_LONG = -0.127758


def is_iss_nearby():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_no <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_nearby() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_add=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: Quick! Look Up!\n\n It's a bird, it's a plane, it's the ISS!",
            )
