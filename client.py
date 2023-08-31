from pymongo import MongoClient

# client (localhst)
client = MongoClient("mongodb://localhost:27017")

# database (sms)
db = client["sms"]

# collection or table
users = db["users"]
secretes = db["secretes"]
