from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister, Showusers
from resources.item import Item, Items
from resources.store import Store, Stores
from models.item import ItemModel
from models.store import StoreModel
from models.user import UserModel
from db import db #import the db which is sqlalchemy object

###############################################################################
app = Flask(__name__)
app.secret_key = "ravish"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #this provides the path of the db to SQLAlchemy
print (app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #This will help in consuming less resources as flask alchemy tries to track all changes
api = Api(app)



jwt = JWT(app, authenticate, identity)
###############################################################################

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Showusers, '/userlist')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Stores, '/storelist')

if __name__ == "__main__":

    print ("Program Started - in main")
    db.init_app(app) #wherever database is used in the models, import the db as well
    app.run(port=5000, debug=True)
