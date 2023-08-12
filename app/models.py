from app import mongo
from bson import ObjectId

class User:
    @staticmethod
    def create_user(data):
        return mongo.db.users.insert_one(data).inserted_id
    
    @staticmethod
    def get_users():
        users = mongo.db.users.find()
        user_list = []
        for user in users:
            user['_id'] = str(user['_id'])  
            user_list.append(user)
        return user_list
    
    @staticmethod
    def get_user(user_id):
        user = mongo.db.users.find_one_or_404({'_id': user_id})
        user['_id'] = str(user['_id']) 
        return user
    
    @staticmethod
    def update_user(user_id, data):
        mongo.db.users.update_one({'_id': user_id}, {'$set': data})
    
    @staticmethod
    def delete_user(user_id):
        mongo.db.users.delete_one({'_id': user_id})
