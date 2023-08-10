from bson import ObjectId
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo


app = Flask(__name__)

# Configure the Flask app to connect to your MongoDB database
app.config['MONGO_URI'] = 'mongodb://localhost:27017/corider'
mongo = PyMongo(app)

# Define the User collection
users = mongo.db.users

@app.route('/users', methods=['GET'])
def get_all_users():
    user_list = []
    for user in users.find():
        user_list.append({
            'id': str(user['_id']),
            'name': user['name'],
            'email': user['email']
        })
    return jsonify(user_list)

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = users.find_one_or_404({'_id': ObjectId(id)})
    return jsonify({
        'id': str(user['_id']),
        'name': user['name'],
        'email': user['email']
    })

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = users.insert_one(data).inserted_id
    return jsonify({'message': 'User created successfully', 'id': str(user_id)})

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    users.update_one({'_id': ObjectId(id)}, {'$set': data})
    return jsonify({'message': 'User updated successfully'})

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    users.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'User deleted successfully'})
