import pymongo
from model.user import User
from time import time


class Database:
    def __init__(self):
        client = pymongo.MongoClient('127.0.0.1', 27017)
        self.db = client['v2ray-user']

    def add(self, doc_or_docs):
        if type(doc_or_docs) is list:
            users = []
            for doc in doc_or_docs:
                user = User(doc['time'] * 30 * 24 * 60 * 60, doc['name'])
                users.append(user.__dict__)
            self.db['user'].insert(users)
        else:
            user = User(doc_or_docs['time'] * 30 * 24 * 60 * 60, doc_or_docs['name'])
            self.db['user'].insert_one(user.__dict__)

    def remove(self, name):
        self.db['user'].delete_many({'name': name})

    def find(self):
        return self.db['user'].find()

    def remove_expiration(self):
        for user in self.db['user'].find():
            if time() > user['expiration_time']:
                self.db['user'].delete_one({'_id': user['_id']})
