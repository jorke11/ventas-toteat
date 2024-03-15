from pymongo import MongoClient

client = MongoClient('mongodb', username='root', password='toor', port=27017)

db = client["languages"]

collection_name = db["collection"]
