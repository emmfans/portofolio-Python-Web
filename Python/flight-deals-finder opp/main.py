#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests,os
import datetime
import notification_manager
from pprint import pprint
import data_manager as dm
import flight_search as fs
from flight_data import FlightData
notif=notification_manager.NotificationManager()
sheety=dm.DataManager()
flightsearch=fs.FlightSearch()
sheet_data=sheety.getdata()
# sheety.loginpage()
users=sheety.getusers()
pprint(sheet_data)
pprint(users)

for i in sheet_data:

    if i["iataCode"]=="":
        iata = flightsearch.checkiata(i['city'])
        sheety.uptadeiata(id=i["id"],data=iata)
    print(i["iataCode"])
    flightdata=flightsearch.search(i["iataCode"])
    try:
        notif.sendemail(flightdata)
    except:
        print("No deal found")









