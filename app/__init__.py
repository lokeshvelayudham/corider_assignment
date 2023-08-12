from flask import Flask
from flask_pymongo import PyMongo
from config import MONGO_URI
from flask_restful import Api

# from app.resources.user_resource import UserResource

# application initalization
app = Flask(__name__)

# db setup and initilazation
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)
api = Api(app)

# from app.models import User
from app.resources.user_resource import user_blueprint
app.register_blueprint(user_blueprint, url_prefix='/users')

# mongo.db.users.create_index([('email', 'unique')])  # Ensure unique emails

# Register resources
# api.add_resource(UserResource, '/users', '/users/<string:user_id>')
