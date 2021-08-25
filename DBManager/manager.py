import pymongo
client = pymongo.MongoClient("mongodb://anjani:<password>@scantaio-shard-00-00.7hc3j.mongodb.net:27017,scantaio-shard-00-01.7hc3j.mongodb.net:27017,scantaio-shard-00-02.7hc3j.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-nhxx0u-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
print(db)