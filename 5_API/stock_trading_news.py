import requests
import smtplib
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
api_key_stock = "-"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
api_key_news = "-"

function = "TIME_SERIES_DAILY"
symbol = STOCK_NAME

parameters = {
    "function": function,
    "symbol": symbol,
    "apikey": api_key_stock
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
print(data)

print(data["Time Series (Daily)"]["2021-01-15"]) #hard coded, but can use list comprehension
day15 = data["Time Series (Daily)"]["2021-01-15"]
day15_closing_data = [price for (num, price) in day15.items()]
day15_closing = day15_closing_data[3]
print(day15_closing)
# yesterday = data["Time Series (Daily)"]["2021-01-15"]["4. close"]
# print(yesterday)

day19 = data["Time Series (Daily)"]["2021-01-19"]
day19_closing_data = [price for (num, price) in day19.items()]
day19_closing = day19_closing_data[3]
print(day19_closing)

difference = abs(float(day19_closing) - float(day15_closing))
rounded_dif = round(difference, 2)
print(rounded_dif)
percentage_dif = rounded_dif/float(day19_closing)*100
round_per_dif = (round(percentage_dif, 2))

if percentage_dif >= 2:

    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": api_key_news
    }

    response_news = requests.get(url=NEWS_ENDPOINT, params=news_parameters)

    response_news.raise_for_status()
    news_data = response_news.json()
    articles = news_data['articles'][:3]
    formatted_article_list = [f"Headline: {article['title']} \nBrief: {article['description']}" for article in articles]

    print(formatted_article_list)
    print(formatted_article_list[0])
    # print(news_data)
    # print(news_data["articles"][0])
    # top_three = news_data["articles"][0:3]
    # # print(top_three)
    # titles = [item["title"] for item in top_three]
    # descriptions = [item["description"] for item in top_three]
    # print(titles)
    # print(descriptions)

   # -----------------------------email---------------------------------------

    my_email = "testpythondy@gmail.com"
    my_password = " "
    yahoo_email = "testpythondy@yahoo.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        for item in formatted_article_list:
            connection.sendmail(
                from_addr=my_email,
                to_addrs=yahoo_email,
                msg=f"Subject: {STOCK_NAME}: 🔺{round_per_dif}\n\n{item}".encode('utf-8'))


   #--------------------------message-------------------------------------------

    account_sid = 'AC1eb47451018293acc406f57cdf4b6dbb'
    auth_token = '-'

    client = Client(account_sid, auth_token)
    for item in formatted_article_list:
        message = client.messages\
            .create(
            body=f"{STOCK_NAME}: UP {round_per_dif}\n\n{item} ",
            from_='+12',
            to='+82'
        )

        print(message.status)