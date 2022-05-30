'''
I am the owner of this template

'''
import json
import datetime
from uuid import uuid4
import re
from test.test_contains import myset
from test.test_enum import Fruit
from test.test_getargs2 import TupleSubclass
import pymongo
from bson.objectid import ObjectId #to Search document with ObjectId
import pprint #Print Json in pretty format


data = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

converttojson = json.dumps(data,indent=1, sort_keys = True)

print(converttojson)

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

database = myclient.list_database_names()
getdatabase = myclient.get_database('tdr')

getAllCollection = getdatabase.list_collection_names()

newCol = 'playwithmong'
if newCol not in getAllCollection :
    getdatabase.create_collection(newCol)
    print ('Database Not Exists but created')
else:
    print ('Database Exists')

for name in getAllCollection:
    print (name)
getCollection = getdatabase.get_collection('sampledata')

query = {'widget.debug': 'on'}
query2 = {'_id': ObjectId("6289958db30cd07b4aebee1a")}
getDocument = getCollection.find(query)

# pprint.pprint(getDocument)

for doc in getDocument: 
   pprint.pprint(dict(doc))
   # print (json.dumps(doc, indent=1, sort_keys = True, default=str))

dt = dict(doc['widget']['image'])
pprint.pprint(dt)

for key,values in dt.items():
    print(f"{key} and {values}") 

'''Using insert one '''
for insertDoc in range(0,4):
    id = uuid4()
    data['_id'] = str(id)
    insertData = getCollection.insert_one(data)
    print(id)

'''Using insert Many '''
list = list()  
for insertDoc in range(0,4):
    id = uuid4()
    data['_id'] = str(id)
    data['count'] = insertDoc
    data['time_stamp'] = str(datetime.datetime.now())
    data_ref = data.copy() 
    list.insert(insertDoc, data_ref)
    
insertData = getCollection.insert_many(list)
# print(getDocument)

