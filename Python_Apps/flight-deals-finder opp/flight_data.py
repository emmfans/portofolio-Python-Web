class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,price,destair,dest,orig,originair,depfrom,depto,stopover="",stopoverair=""):
        self.price=price
        self.destair=destair
        self.dest=dest
        self.orig=orig
        self.originair=originair
        self.depfrom=depfrom
        self.depto=depto
        self.stopover=stopover
        self.stopoverair=stopoverair