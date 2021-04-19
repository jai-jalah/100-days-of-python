import datetime as dt
import smtplib
import random

MY_EMAIL = "testjai22@gmail.com"
MY_PASSWORD = "jaiwastesting222"

now = dt.datetime.now()
day_of_the_week = now.weekday()

if day_of_the_week == 1:
    with open("quotes.txt") as quote_file:
        quotes = quote_file.readlines()
        quote = random.choice(quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="test.jai@yahoo.com",
            msg=f"Subject: Pipe up!\n\n{quote}",
        )
