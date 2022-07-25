import pymongo
client = pymongo.MongoClient("mongodb+srv://mdbUser:mdbUser108@cluster0.o52iclm.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "Parnika",
    "Surname" : "Patil",
    "email" : "parnika.d.patil@gmail.com"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)