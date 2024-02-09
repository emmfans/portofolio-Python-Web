import smtplib
from flight_data import FlightData
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.username="xxxxxxxxxx"
        self.password="xxxxxxxxxxxxxxxxxx"

    def sendemail(self,flighdata):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as ct:
            ct.starttls()
            ct.login(self.username,self.password)
            ct.sendmail(
                from_addr=self.username,
                to_addrs="xxxxxxxxxxxx",
                msg=f"Subject:New deal for {flighdata.dest}\n\nNew deal for{flighdata.dest}!!.Only {flighdata.price}Eu to fly from {flighdata.orig}-{flighdata.originair} to {flighdata.dest}-{flighdata.destair}.From {flighdata.depfrom} to {flighdata.depto}(Gr Time)"
            )
