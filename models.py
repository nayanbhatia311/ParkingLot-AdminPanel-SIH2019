from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.parkinglots
user=db["Userinfo"]

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
        b=db.fromUser.find({},{"_id":0})
        print(b)
        bc=[]
        for i in b :
            bc.append(i)
        print(bc)
        return bc
