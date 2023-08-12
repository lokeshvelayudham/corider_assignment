from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource, reqparse
from app.models import User
from bson import ObjectId


user_blueprint = Blueprint('user', __name__)
api = Api(user_blueprint)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('email', type=str)
parser.add_argument('password', type=str)

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            return User.get_user(ObjectId(user_id))
        else:
            return User.get_users()
    
    def post(self):
        args = parser.parse_args()
        user_id = User.create_user(args)
        return {'message': 'User created', 'user_id': str(user_id)}, 201
    
    def put(self, user_id):
        args = parser.parse_args()
        User.update_user(ObjectId(user_id), args)
        return {'message': 'User updated'}, 200
    
    def delete(self, user_id):
        User.delete_user(ObjectId(user_id))
        return {'message': 'User deleted'}, 200

api.add_resource(UserResource, '/', '/<string:user_id>')