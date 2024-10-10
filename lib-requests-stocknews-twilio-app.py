import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")   
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")   

# *******************************************************************************
# Setup an account at https://www.alphavantage.co
# to get the Key.
# *******************************************************************************
STOCK_ENDPOINT = os.environ.get("STOCK_ENDPOINT")  
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")  

# *******************************************************************************
# Setup an account at https://newsapi.org
# to get the Key.
# *******************************************************************************
NEWS_ENDPOINT = os.environ.get("NEWS_ENDPOINT")  
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")  

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME, # "IBM", #
    "apikey": STOCK_API_KEY, # "demo",  #
}

# 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
data = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
data.raise_for_status()
daily_data = [value for (key, value) in data.json()["Time Series (Daily)"].items()]
# print(daily_data)
yesterday_close = float(daily_data[0]['4. close'])

# 2. - Get the day before yesterday's closing stock price
day_before_close = float(daily_data[1]['4. close'])
print(f"{yesterday_close}, {day_before_close}")

# 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
price_diff = yesterday_close - day_before_close
price_diff_abs = abs(price_diff)

# 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_diff = price_diff_abs*100/yesterday_close

# 5. - If percentage is greater than 5 then print("Get News").
if percentage_diff > 5:
    print("Get News")
else:
    print(f"Pricing was stable last two days - only {percentage_diff:.2f}% change")

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
# https://newsapi.org/v2/everything?q=Tesla%20Inc&pageSize=5&sortBy=publishedAt&apiKey=<API_KEY>
news_parameters = {
    "q": COMPANY_NAME,
    "pageSize": 5,
    "sortBy": "publishedAt",
    "apiKey": NEWS_API_KEY,
}
response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
response.raise_for_status()
data = response.json()


# 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
news_data = data["articles"][:3]
# print(news_data)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
news_data_filtered = [(article["title"], article["description"]) for article in news_data]
# print(news_data_filtered)

#TODO 9. - Send each article as a separate message via Twilio. 

for news in news_data_filtered:
    message = f"{STOCK_NAME}: "
    if price_diff > 0:
        message += "🔺"
    else:
        message += "🔻"
    message += f"{percentage_diff:.2f}%\nHeadline: {news[0]}\nBrief: {news[1]}"
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message,
        from_="whatsapp:+14155238886",  # for SMS - need extra verification - +18882314251",
        to="whatsapp:+17162819655",
    )
    print(message.status)



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

