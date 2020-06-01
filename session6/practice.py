from pymongo import MongoClient
from bson.objectid import ObjectId              

client = MongoClient()

db = client.get_database('mongo_practice')

movie_collection = db.get_collection('movies')

data = [
{   'title' : 'Fight Club',
    'writer' : 'Chuck Palahniuk',
    'year' : 1999,
    'actors' : [
    'Brad Pitt',
    'Edward Norton'
    ]
},

{   
    'title' : 'Pulp Fiction',
    'writer' : 'Quentin Tarantino',
    'year' : 1994,
    'actors' : [
    'John Travolta',
    'Uma Thurman'
    ]
},

{   'title' : 'Inglorious Basterds',
    'writer' : 'Quentin Tarantino',
    'year' : 2009,
    'actors' : [
    'Brad Pitt',
    'Diane Kruger',
    'Eli Roth'
    ]
},

{   'title' : 'The Hobbit: An Unexpected Journey',
    'writer' : 'J.R.R. Tolkein',
    'year' : 2012,
    'franchise' : 'The Hobbit'
},

{   
    'title' : 'The Hobbit: The Desolation of Smaug',
    'writer' : 'J.R.R. Tolkein',
    'year' : 2013,
    'franchise' : 'The Hobbit'
},

{
    'title' : 'The Hobbit: The Battle of the Five Armies',
    'writer' : 'J.R.R. Tolkein',
    'year' : 2012,
    'franchise' : 'The Hobbit',
    'synopsis' : 'Bilbo and Company are forced to engage in a war against an array of combatants and keep the Lonely Mountain from falling into the hands of a rising darkness.'
},

{
    'title' : "Pee Wee Herman's Big Adventure"
},

{
    'title' : 'Avatar'
}

]

## 1. get all documents
# movie_collection.insert_many(data)

## 2. get all documents with 'writer' set to "Quentin Tarantino"
# for movie in data:
#     if movie['writer'] == "Quentin Tarantino":
#         print(movie['title'])

# for movie in movie_collection.find({ "writer": 'Quentin Tarantino' }):
#   print(movie['title'])


## 3.get all documents where actors include "Brad Pitt"
# for movie in data:
#     if 'actors' in movie: 
#         if 'Brad Pitt' in movie['actors']:
#             print(movie['title'])

# for movie in movie_collection.find({ "actors": 'Brad Pitt' }):
#   print(movie['title'], movie['actors'])


## 4.get all documents with 'franchise' set to "The Hobbit"
# for movie in movie_collection.find({ "franchise": 'The Hobbit' }):
#   print(movie['title'], movie['franchise'])

## 5.get all movies released in the 90s
# for movie in movie_collection.find({ "year": {'$gte': 1990, '$lt': 2000} }):
#     print(movie['title'], movie['year'])

## 6. get all movies released before the year 2000 or after 2010
# for movie in movie_collection.find({ '$or': [ {'year': {'$gt': 2010}}, {'year': {'$lt': 2000}} ]   }):
#     print(movie['title'], movie['year'])

#### UPDATE ####
## 1.add a synopsis to "The Hobbit: An Unexpected Journey"
# query = { "title": "The Hobbit: An Unexpected Journey" }
# new1 = { "$set": { "synopsis": "A reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug." } } 
# movie_collection.update_one(query, new)

# for movie in movie_collection.find():
#   print(movie)


## 2. add a synopsis to "The Hobbit: The Desolation of Smaug" :
# query = { "title": "The Hobbit: The Desolation of Smaug" }
# new = { "$set": { 'synopsis': "The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring." } } 
# movie_collection.update_one(query, new)

# for movie in movie_collection.find():
#   print(movie)

## 3.add an actor named "Samuel L. Jackson" to the movie "Pulp Fiction"
# query = { "title": "Pulp Fiction" }
# new = { "$push": { 'actors': 'anh Huấn Hoa Hồng' } } 
# movie_collection.update_one(query, new)

# for movie in movie_collection.find():
#   print(movie)

#### Text Search #### 
## 1. find all movies that have a synopsis that contains the word "Bilbo"
# for movie in movie_collection.find({ "synopsis" : {'$regex' : ".*Bilbo.*"}  }):
#   print(movie['title'], movie['synopsis'])

## 2. find all movies that have a synopsis that contains the word "Gandalf"
# for movie in movie_collection.find({ "synopsis" : {'$regex' : ".*Gandalf.*"}  }):
#   print(movie['title'], movie['synopsis'])

## 3. find all movies that have a synopsis that contains the word "Bilbo" and not the word "Gandalf"
# for movie in movie_collection.find(
#     {
#         '$and': [ 
#             {"synopsis" : {'$regex' : ".*Bilbo.*"}}, 
#             {"synopsis" : {'$not': {'$regex' : ".*Gandalf.*"}}} 
#         ] 
#     }
# ):
#   print(movie['title'], movie['synopsis'])

## 4. find all movies that have a synopsis that contains the word "dwarves" or "hobbit"
# for movie in movie_collection.find({'$or': [ {"synopsis" : {'$regex' : ".*dwarves.*"}}, {"synopsis" : {'$regex' : ".*hobbit.*"}} ] }):
#   print(movie['title'], movie['synopsis'])

## 5. find all movies that have a synopsis that contains the word "gold" and "dragon"
# for movie in movie_collection.find(
#     {
#         '$and': [ 
#             {"synopsis" : {'$regex' : ".*gold.*"}}, 
#             {"synopsis" : {'$regex' : ".*dragon.*"}} 
#         ] 
#     }
# ):
#   print(movie['title'], movie['synopsis'])

### DELETE ###
## 1.delete the movie "Pee Wee Herman's Big Adventure"
# query = {
#     'title': "Pee Wee Herman's Big Adventure"
# }
# movie_collection.delete_one(query)
# for movie in movie_collection.find():
#   print(movie)

## 2.delete the movie "Avatar"
# query = {
#     'title': "Avatar"
# }
# movie_collection.delete_one(query)
# for movie in movie_collection.find():
#   print(movie)

#### UPDATE ####
# CREATE USERS COLLECTION
data2 = [
    {
        'username' : 'GoodGuyGreg',
        'first_name' : "Good Guy",
        'last_name' : "Greg"
    },
    {
        'username' : 'ScumbagSteve',
        'full_name' : {
            'first': 'Scumbag',
            'last' : 'Steve'
        }
    }
]

db = client.get_database('mongo_practice')

user_collection = db.get_collection('users')

# user_collection.insert_many(data2)


# CREATE POSTS COLLECTION

data3 = [
    {
        'username' : 'GoodGuyGreg',
        'title' : 'Passes out at party',
        'body' : 'Wakes up early and cleans house'
    },
    {
        'username' : 'GoodGuyGreg',
        'title' : 'Steals your identity',
        'body' : 'Raises your credit score',
    },
    {
        'username' : 'GoodGuyGreg',
        'title' : 'Reports a bug in your code',
        'body' : 'Sends you a Pull Request',
    },
    {
        'username' : 'ScumbagSteve',
        'title' : 'Borrows something',
        'body' : 'Sells it',
    },    
    {
        'username' : 'ScumbagSteve',
        'title' : 'Borrows everything',
        'body' : 'The end',
    },
    {
        'username' : 'ScumbagSteve',
        'title' : 'Forks your repo on github',
        'body' : 'Sets to private',
    }
    
]

db = client.get_database('mongo_practice')

post_collection = db.get_collection('posts')

# post_collection.insert_many(data3)


### CREATE COMMENTS COLLECTION

db = client.get_database('mongo_practice')

comment_collection = db.get_collection('comments')

data4 = [
    {
        'username' : 'GoodGuyGreg',
        'title' : 'Hope you got a good deal!',
        'post' : '5ed3c9519d0c2243e745b643'
    },
    {
        'username' : 'GoodGuyGreg',
        'title' : "What's mine is yours!",
        'post' : '5ed3c9519d0c2243e745b644'
    },
    {
        'username' : 'GoodGuyGreg',
        'title' : "Don't violate the licensing agreement!",
        'post' : '5ed3c9519d0c2243e745b645'
    },
    {
        'username' : 'GoodGuyGreg',
        'title' : "It still isn't clean",
        'post' : '5ed3c9519d0c2243e745b640'
    },
    {
        'username' : 'GoodGuyGreg',
        'title' : "Denied your PR cause I found a hack",
        'post' : '5ed3c9519d0c2243e745b642'        
    }
]

# comment_collection.insert_many(data4)

# print(comment_collection)

# 1. Find all users
# print('--- All users ---')
# for user in user_collection.find(
#     {}
# ):
#     print(user['username'])
# print()

# 2. Find all posts
# print('--- All posts ---')
# for post in post_collection.find(
#     {}
# ):
#     print(post['title'])
# print()

# 3. find all posts that was authored by "GoodGuyGreg"
# print('--- Posts by GoodGuyGreg ---')
# for post in post_collection.find(
#     {'username': 'GoodGuyGreg'}
# ):
#     print(post['title'])
# print()

# 4. find all posts that was authored by "ScumbagSteve"
# print('--- Posts by ScumbagSteve ---')
# for post in post_collection.find(
#     {'username': 'ScumbagSteve'}
# ):
#     print(post['title'])
# print()

# 5.find all comments
# print('--- All comments ---')
# for comment in comment_collection.find(
#     {}
# ):
#     print(comment['username'], ':', comment['title'])
# print()

# 6. find all comments that was authored by "GoodGuyGreg"
# print('--- Comments by GoodGuyGreg ---')
# for comment in comment_collection.find(
#     {'username': 'GoodGuyGreg'}
# ):
#     print(comment['title'])
# print()

# 7.find all comments that was authored by "ScumbagSteve"
# print('--- Comments by ScumbagSteve ---')
# for comment in comment_collection.find(
#     {'username': 'ScumbagSteve'}
# ):
#     print(comment['title'])
# print()

## cop nhầm nên phải sửa lại
# query = { "title": "Denied your PR cause I found a hack" }
# new = { "$set": { 'username': "ScumbagSteve" } } 
# comment_collection.update_one(query, new)

# 8. find all comments belonging to the post "Reports a bug in your code"
print('--- Comments related to post Reports a Bug ---')
for comment in comment_collection.find(
    {
        'post': str(post_collection.find_one(
            {
                'title': "Reports a bug in your code"
            }
            )
            ['_id'])
    }
):
    print(comment['title'])


