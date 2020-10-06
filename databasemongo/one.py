import pymongo
from pymongo import MongoClient
client = MongoClient(port=27017)

db = client.shop
collectionName = db.products

doc_one = collectionName.find_one({'name':"A book"})
print(doc_one)

doc_all = collectionName.find()
print(doc_all)