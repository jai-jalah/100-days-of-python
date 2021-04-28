from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

TARGET = "https://www.amazon.co.uk/Basketball-Elastic-Cushioning-Lightweight-Trainers/dp/B07KW1GBLR/ref=sr_1_6?dchild=1&keywords=basketball+shoes&qid=1619626899&sr=8-6"
HEADERS = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
}

response = requests.get(url=TARGET, headers=HEADERS)
response.raise_for_status()
webpage_html = response.text

soup = BeautifulSoup(webpage_html, "lxml")
soup_price = soup.find("span", id="priceblock_ourprice").get_text()
if "-" in soup_price:
    lowest_price = soup_price.split("-")
    soup_price = float(lowest_price[0].strip("£"))

print(soup_price)