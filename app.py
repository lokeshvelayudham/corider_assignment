# # import flask and pyMongo, bson
# from bson import ObjectId
# from flask import Flask, jsonify, request
# from flask_pymongo import PyMongo


# app = Flask(__name__)

# # Configure the Flask app to connect to your MongoDB database
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/corider'
# mongo = PyMongo(app)

# # Define the User collection
# users = mongo.db.users


# # GET /users - Returns a list of all users.
# @app.route('/users', methods=['GET'])
# def get_all_users():
#     user_list = []
#     for user in users.find():
#         user_list.append({
#             'id': str(user['_id']),
#             'name': user['name'],
#             'email': user['email']
#         })
#     return jsonify(user_list)



# # GET /users/<id> - Returns the user with the specified ID.
# @app.route('/users/<id>', methods=['GET'])
# def get_user(id):
#     user = users.find_one_or_404({'_id': ObjectId(id)})
#     return jsonify({
#         'id': str(user['_id']),
#         'name': user['name'],
#         'email': user['email']
#     })


# # POST /users - Creates a new user with the specified data.
# @app.route('/users', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     user_id = users.insert_one(data).inserted_id
#     return jsonify({'message': 'User created successfully', 'id': str(user_id)})


# # PUT /users/<id> - Updates the user with the specified ID with the new data.
# @app.route('/users/<id>', methods=['PUT'])
# def update_user(id):
#     data = request.get_json()
#     users.update_one({'_id': ObjectId(id)}, {'$set': data})
#     return jsonify({'message': 'User updated successfully'})


# # DELETE /users/<id> - Deletes the user with the specified ID.
# @app.route('/users/<id>', methods=['DELETE'])
# def delete_user(id):
#     users.delete_one({'_id': ObjectId(id)})
#     return jsonify({'message': 'User deleted successfully'})
