from pymongo import MongoClient




class Mongo:
    def __init__(self,db,collections):
        self.collections = [] #data base's collections
        client = MongoClient("mongodb://taoufik:NrV3lUnwEJcebw9m@ttproject-shard-00-00-oyx2l.mongodb.net:27017,ttproject-shard-00-01-oyx2l.mongodb.net:27017,ttproject-shard-00-02-oyx2l.mongodb.net:27017/test?ssl=true&replicaSet=TTProject-shard-0&authSource=admin&retryWrites=true")
        self.db = client[db]
        for collection in collections:
            self.collections.append({'name':collection, 'obj' : self.db[collection]})

    def insert(self,document,collection):
        for coll in self.collections:
            if coll['name'] == collection:
                coll['obj'].insert_one(document)

        
    
    def find(self,collection,feild,value):
        for coll in self.collections:
            if coll['name'] == collection:
                result =  coll['obj'].find({feild : value})
                return result
        






        
