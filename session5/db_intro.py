from pymongo import MongoClient

client = MongoClient()

db = client.get_database('thonau')                  #Mongo rất thông minh

member_collection = db.get_collection('members')

# member_collection.insert_one()

data1 = {
    'name': 'Quyen',
    'age': 27,
    'rela' : False
}

data2 = {
    'name': 'Thao',
    'age': 18,
    'rela' : True
}

member_collection.insert_one(data1)      #insert a record to collection
# member_collection.insert_one(data2)      #insert a record to collection


members = member_collection.find()         #GET ALL RECORDS

for member in members:
    print(member)