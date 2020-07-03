from app import app
from db import db

db.init_app(app)

#the below lines will ensure that sqlalchemy creates a table automatically for us, and we dont have to create it everytime
#for this, we use the decorator as follows before any of the reqeusts are being made:
#this is a flask decorator, hence app.
@app.before_first_request
def create_tables():
    db.create_all()# this will first create the data.db and then the tables if they are not there.
