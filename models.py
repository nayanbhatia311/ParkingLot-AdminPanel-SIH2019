from pymongo import MongoClient
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, IntegerField
import bson.json_util as bsj
import json
from bson.objectid import ObjectId
from flask import jsonify

session = False

client = MongoClient("mongodb://localhost:27017")
db = client.parkinglots
user=db["Userinfo"]
fromU = db["fromUser"]

class UserModel():
    def getUser(self):
        x = db.Userinfo.find({},{"_id":0})
      #  print(x)
        abc =[]
        for i in x :
            abc.append(i)
        return abc

class PayandParking():
    def getPay(self):
        a=db.PayandParking.find({},{"_id":0})
        print(a) 
        ab=[]
        for i in a:
            ab.append(i)
        return ab

class FromUser():
    def fromuser(self):
        b=db.fromUser.find({})
        #print(b)
        bc=[]
        for i in b :
            bc.append(i)
        x = bsj.dumps(bc)
        # print(type(x))
        qa = json.loads(x)
        # print(type(qa))
        # print(qa[0]["properties"]["name"])
        # print(qa[0]["_id"]["$oid"])
        # print(qa)
        #print(x[0]["properties"]["description"])
        # for z in x:
        #     y = z.it
        # print (y)
        return qa

# class ReusableForm(Form):
#     name = TextField('Name:', validators=[validators.required()])
#     address1 = TextField('Address1:', validators=[validators.required())
#     address2 = TextField('Address2:', validators=[validators.required())
#     city = TextField('City:', validators=[validators.required()])
#     latitude = TextField('Latitude:', validators=[validators.required()])
#     longitude = TextField('Longitude:', validators=[validators.required()])
#     capacity = TextField('Capacity:', validators=[validators.required()])
#     days = TextField('Days:', validators=[validators.required()])
#     restrictions = TextField('Restrictions:')
#     category = TextField('Category:', validators=[validators.required()])
#     timing = TextField('Time', validators=[validators.required()])
#     chargesperhour = TextField('Charges Per Hour')


class CreateLot():
    def __init__(self,name,address1,address2,city,latitude,longitude,capacity,days,restrictions,category,timing,chargesperhour):
        self.name = name
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.capacity = capacity
        self.days = days
        self.restrictions = restrictions
        self.category = category
        self.timing = timing
        self.chargesperhour = chargesperhour
    def insert(self):
            disstring = "{},{},{},{},{},{},{},{},{},{},{}"
            discription = disstring.format(self.name , self.address1 , self.address2 , self.city , self.latitude , self.longitude , self.capacity , self.days , self.restrictions , self.category , self.timing , self.chargesperhour)
            addstring = "{},{}"
            address = addstring.format(self.address1,self.address2)
            t = db.fromUser.insert({
                    "type": "Feature",
                    "properties": {
                    "name": self.name,
                    "description": discription,
                    "parkingId": "",
                    "city": self.city,
                    "road": self.address1,
                    "landmark": self.address2,
                    "address": address,
                    "latitude": self.latitude,
                    "longitude": self.longitude,
                    "capacity": self.capacity,
                    "days": self.days,
                    "direction": "",
                    "restrictions": "",
                    "towingStation": "",
                    "category": self.category,
                    "status new": "",
                    "timing": self.timing,
                    "charging_hour": self.chargesperhour,
                    "vehicalType": "",
                    "charges": "",
                    "vehicleTypeId": "",
                    "dislikes":0,
                    "likes":0
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            self.longitude,
                            self.latitude
                        ]
                    }})
            print(t)
            return jsonify(t)
class Deletion():
    def __init__(self,Obj):
        self.Obj = Obj
    def dele(self):
        y = ObjectId(self.Obj)
        db.fromUser.remove({"_id":y})

