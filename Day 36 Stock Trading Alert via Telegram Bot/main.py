STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

import requests
from password import stock_api_key,news_api_key,bot_token,chat_id
from datetime import datetime,timedelta

def send_telegram_message(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id \
                + '&parse_mode=Markdown&text=' + bot_message

    bot_response = requests.get(send_text)
    return bot_response.json()
   


stock_api_url=f"https://www.alphavantage.co/query"
stock_params={
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": stock_api_key
}
response=requests.get(stock_api_url, params=stock_params)
response.raise_for_status()    
stock_data=response.json()

yesterday = datetime.now() - timedelta(days=2)
yesterday_date=yesterday.strftime('%Y-%m-%d')
day_before_yesterday=datetime.now() - timedelta(days=3)
day_before_date=day_before_yesterday.strftime('%Y-%m-%d')
stock_data_yesterday=float(stock_data["Time Series (Daily)"][yesterday_date]["4. close"])
stock_data_day_before=float(stock_data["Time Series (Daily)"][day_before_date]["4. close"])
diff=stock_data_yesterday-stock_data_day_before
if diff>0:
    up_down="⬆️"
else:
    up_down="⬇️"

difference = abs(diff)
percentage_difference = round((difference/stock_data_day_before)*100)
if percentage_difference>=5:
   news_api=f"https://newsapi.org/v2/everything"
   news_params={
       "q":COMPANY_NAME,
       "apiKey":news_api_key
        }
   response=requests.get(news_api, params=news_params)
   response.raise_for_status()    
   news_data=response.json()
   for article in range(3):
    market_performamce=f"{STOCK}:{up_down} {percentage_difference}%"
    title=news_data["articles"][article]["title"]
    brief=news_data["articles"][article]["description"]
    news=(f"{market_performamce}\n{title}\n{brief}\n")
    print(send_telegram_message(news))
    
