import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.urlsh="xxxxxxxxx"
        self.bearer="xxxxxxxxxx"
        self.header={
            "Authorization": self.bearer
        }
    def getdata(self):
        endpoint = self.urlsh + f"/prices"
        response = requests.get(url=endpoint, headers=self.header).json()
        return response["prices"]
    def getusers(self):
        endpoint = self.urlsh + f"/users"
        response = requests.get(url=endpoint, headers=self.header).json()
        return response["users"]
    def uptadeiata(self,data,id):

        param={
            "price":{
                'iataCode':data
            }
        }
        endpoint=self.urlsh+f"/prices/{id}"
        response=requests.put(url=endpoint, json=param,headers=self.header)
        print(response.raise_for_status())
    def uptadeuser(self,email,fname,lname):

        param={
            "user":{
                'email':email,
                'firstName':fname,
                'lastName':lname
            }
        }
        endpoint=self.urlsh+f"/users"
        response=requests.post(url=endpoint, json=param,headers=self.header)
        print(response.raise_for_status())

    def loginpage(self):
        users = self.getusers()
        print("Welcome to Nikis Deals Club!!!\nWe have the best deals for you")
        Fname=input("What is your first name\n")
        Lname = input("What is your last name\n")
        add=True
        for users in users:
            if users["firstName"]==Fname and Lname==users["lastName"]:
                add=False
        if  add:
            Email = input("What is your email\n")
            email = input("confirm email\n")
            while (email != Email):
                    Email = input("What is your email\n")
                    email = input("confirm email\n")
            print("You are in the club")
            self.uptadeuser(email, Fname, Lname)

        else:
            print("User already in Da CLUB")









