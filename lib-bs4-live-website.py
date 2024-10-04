import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv


load_dotenv()

AMAZON_IP_URL_PRACTICE = "https://appbrewery.github.io/instant_pot/"
AMAZON_IP_URL_LIVE = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
TARGET_PRICE = 100

SMTP_ADDRESS = os.environ["SMTP_ADDRESS"]
SMTP_PORT = int(os.environ["SMTP_PORT"])
EMAIL_ADDRESS = os.environ["EMAIL_ADDRESS"]
# the app password needs to be set under your google account and pasted here.
# to set it, sign-in after enabling 2-step verification and click on App Password -
# Google might be moving away from this as there is a note that says to use
# "sign in with google" instead of App passwords
APP_PASSWORD = os.environ["APP_PASSWORD"]

# WHY ARE HEADERS NEEDED?
#
# If you pass some headers along then Amazon's servers can give you the instant 
# pot page in your language and also in your currency.
#
# Also, it will make your request look (slightly) more human and less like a bot. 
# Why? Headers include data that is sent over by a browser rather than a script. 
# And many web servers like Amazon's may block requests they think originate from bots.
#
# By using the headers, Amazon's server can respond with the right website for your 
# region and your language.
#
# See the headers that your own browser is sending by going to this website: 
#   http://myhttpheader.com/
#
# the header template used below copies from https://httpbin.org/headers with host 
# and X-Amzn-Trace-Id keys removed
HTTP_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
  }
# A minimal header would look like this:
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }

# response = requests.get(AMAZON_IP_URL_LIVE, headers=HTTP_HEADERS)
response = requests.get(AMAZON_IP_URL_PRACTICE, headers=HTTP_HEADERS)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
price_whole_tag = soup.find(name="span", attrs={"class": "a-price-whole"})
price_whole = int(str(price_whole_tag.contents[0]))
# print(price_whole)

price_fraction_tag = soup.find(name="span", attrs={"class": "a-price-fraction"})
price_fraction = int(price_fraction_tag.text)
# print(price_fraction)
price = int(price_whole) + price_fraction/100
# print(f"{price:.2f}")

if price <= TARGET_PRICE:
    product_title_tag = soup.find(name="span", attrs={"id": "productTitle"})
    product_title = product_title_tag.text.strip()
    # print(product_title)
    with smtplib.SMTP(SMTP_ADDRESS, SMTP_PORT) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=APP_PASSWORD)
        connection.sendmail(from_addr=EMAIL_ADDRESS,
                            to_addrs="JohnKonnayilVincent@gmail.com",
                            msg=f"Subject: Amazon Price Alert!\n\n{product_title} is now {price:.2f}.\n{AMAZON_IP_URL_LIVE}".encode("utf-8"))
