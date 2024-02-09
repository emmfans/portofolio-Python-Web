
import requests,smtplib
from datetime import date,timedelta

now=date.today()
lyest=now -timedelta(days = 2)
yest=now -timedelta(days = 1)

stocksap="xxxxxxxxxxxxxx"
newsap='xxxxxxxxxxxxxxxxx'
passw='xxxxxxxxxxxxxxxxxxxxxxxx'
email='xxxxxxxxxxxxxxxxxxxxx@gmail.com'

with open(file="STOCK") as fl:
    stock=fl.readlines()
stock=[stock.strip() for stock in stock]
for stock in stock:
    paramstock={
        'function':'TIME_SERIES_DAILY',
        'symbol':stock,
        'apikey':stocksap
    }


    stockdata=requests.get('https://www.alphavantage.co/query',params=paramstock).json()

    # Time Series (Daily)►2024-01-10►4. close
    closepricelast=stockdata['Time Series (Daily)'][f"{yest}"]['4. close']
    closepricebeforelast=stockdata['Time Series (Daily)'][f"{lyest}"]['4. close']

    change=((float(closepricelast)-float(closepricebeforelast))/float(closepricelast))*100
    change=round(change, 2)

    if change>0:
        change=f"+{change}%"
    else:
        change = f"-{change}%"

    param={
        'apiKey':newsap,
        'searchIn':'content',
        'q':f"{stock} stock",
        "from":yest,
        "sortBy":"relevancy",
        "language":'en'
    }

    news=requests.get("https://newsapi.org/v2/everything",params=param).json()
    content=news['articles'][0]["description"]
    url=news['articles'][0]["url"]

    subject=f"{yest} changes to {stock}"
    message=f"{yest} closing price is {closepricelast} with a change of {change} \n\n. Most recent article about {stock} is : {content} \n-with a url : {url}"
    message.encode('utf-8')

    with smtplib.SMTP("smtp.gmail.com",port='587') as ct:
        ct.starttls()
        ct.login(email,passw)
        ct.sendmail(
            from_addr=email,
            to_addrs='xxxxxxxxxxxxxxxxxxxxxxxxxxx@gmail.com',
            msg=f'Subject:{subject}\n\n{message}'.encode('utf-8')
        )