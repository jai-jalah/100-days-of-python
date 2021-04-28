from bs4 import BeautifulSoup
import requests
import lxml
from decouple import config
import smtplib

TARGET_URL = "https://www.amazon.co.uk/Basketball-Elastic-Cushioning-Lightweight-Trainers/dp/B07KW1GBLR/ref=sr_1_6?dchild=1&keywords=basketball+shoes&qid=1619626899&sr=8-6"
HEADERS = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
}
MY_EMAIL = config("MY_EMAIL")
MY_PASSWORD = config("MY_PASSWORD")
BUY_PRICE = 35

response = requests.get(url=TARGET_URL, headers=HEADERS)
response.raise_for_status()
webpage_html = response.text

soup = BeautifulSoup(webpage_html, "lxml")
price = soup.find("span", id="priceblock_ourprice").get_text()
if "-" in price:
    lowest_price = price.split("-")
price = float(lowest_price[0].strip("£"))

# print(price)

product_title = soup.find(id="productTitle").get_text().strip()
# print(title)

if price < BUY_PRICE:
    message = f"{product_title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{TARGET_URL}".encode(
                "utf8"
            ),
        )
