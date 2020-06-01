from pymongo import MongoClient

client = MongoClient()

db = client.get_database('thotrang')

member_collection = db.get_collection('members')

data1 = {
    'name': 'Quyen',
    'age': 200,
    'relationship': False,
    'characters': ['short', 'cute', 'waggling tail']
}

data2 = {
    'name': 'Thao',
    'nice_level': 3000,
    'characters': ['nice', 'tall', 'beautiful']
}

# member_collection.insert_many([data1, data2])

members = member_collection.find()

for member in members:
    if 'nice_level' in member:
        print(member['name'])


# for member in members:
#     print(member[age])
