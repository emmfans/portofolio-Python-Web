import requests
import datetime
from pprint import pprint
from flight_data import FlightData
class FlightSearch:
    def __init__(self):
        self.api="xxxxxxxxx"
        self.url="https://api.tequila.kiwi.com"
        self.header={
            "apikey":self.api,

        }
        self.depfrom=(datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%d/%m/%Y")
        self.depto=(datetime.datetime.now()+datetime.timedelta(days=180)).strftime("%d/%m/%Y")

    def checkiata(self,data):
        endpoint=self.url+"/locations/query"
        param={
            "term":data,
            "location_types":"city"
        }
        response=requests.get(url=endpoint,params=param,headers=self.header)
        print(response.raise_for_status())
        response=response.json()
        return response["locations"][0]["code"]

    def search(self,iata,stopover=0):

        endpoint=self.url+"/search"
        param={
            "date_from":self.depfrom,
            "date_to":self.depto,
            "nights_in_dst_from":3,
            "nights_in_dst_to":7,
            "fly_from":"ATH",
            "fly_to":iata,
            "cur":"EUR",
            "one_for_city":1,
            "max_stopovers":stopover

        }

        response = requests.get(url=endpoint, params=param, headers=self.header)
        try:
            data = response.json()["data"][0]
            print(response.raise_for_status())


        except IndexError:
            return None
 

        else :

                data = response.json()["data"][0]
                flight_data=FlightData(price=data["price"],
                                           destair=data["route"][0]["flyTo"],
                                           dest=data["route"][0]["cityTo"],
                                           orig=data["route"][0]["cityFrom"],
                                           originair=data["route"][0]["flyFrom"],
                                           depfrom=datetime.datetime.fromtimestamp(data["route"][0]["dTimeUTC"]),
                                           depto=datetime.datetime.fromtimestamp(data["route"][1]["dTimeUTC"]))
                return flight_data




   