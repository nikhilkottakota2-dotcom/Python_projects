import requests
import os 
import smtplib
STOCK_NAME = "IBM"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
COMPANY_NAME = "ibm"
STOCK_KEY = os.environ.get("STOCK_KEY")
NEWS_KEY = os.environ.get("NEWS_KEY")
MAIL_PASS = os.environ.get("MAIL_PASS")
MAIL_ID = os.environ.get("MAIL_ID")
def mail():
    formatted_articles = ""

    for article in three_articles:
        title = article.get("title") or "No title"
        description = article.get("description") or "No description"
        url = article.get("url") or "No URL"

        formatted_articles += (
            f"Title: {title}\n\n"
            f"Description: {description}\n\n"
            f"Read more: {url}\n"
            f"{'-' * 50}\n\n"
        )

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MAIL_ID,MAIL_PASS)
        message = f"Subject:Stock change\n\n{formatted_articles}"
        connection.sendmail(
            from_addr=MAIL_ID,
            to_addrs="nikhilkottakota2@gmail.com",
            msg=message.encode("utf-8")
        )
stocks_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_KEY
}

news_params = {
    "qInTitle":COMPANY_NAME,
    "sortBy":"publishedAt",
    "apiKey":NEWS_KEY
}


#stocks requests
stocks_response = requests.get(STOCK_ENDPOINT,params=stocks_params)
data = stocks_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

# yesterday price

yesterday_data = data_list[0] 
yesterday_closing_price = yesterday_data["4. close"]

#day before yesterday price

day_before_yesterday_data = data_list[0]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price)-float(day_before_yesterday_closing_price)


diff_percent =  6#(difference/float(day_before_yesterday_closing_price)) * 100
print(diff_percent)

if diff_percent > 5:
    news_response = requests.get(NEWS_ENDPOINT,params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    mail()

