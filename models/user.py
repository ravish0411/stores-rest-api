import sqlite3
from db import db

class UserModel(db.Model): #extend the classes so that the alchemy can be interacted with

#include the tables used in the class as below:
    __tablename__ = 'users'
    #next is to inform db about the columns:
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))

    def __init__(self, username, password):
        print ("Creating UserModel:")
        self.username = username
        self.password = password

#as the self is not used in the below function, we can build  class method
    @classmethod
    def find_by_username(cls, username):

        return cls.query.filter_by(username = username).first()

    @classmethod
    def find_by_userid(cls, userid):

        return cls.query.filter_by(id = userid).first()

    def save_user_to_db(self):

        print ("in model")
        print (self.id)
        print (self.username)
        print (self.password)
        db.session.add(self)
        db.session.commit()
        user = UserModel.query.filter_by(username = self.username).first()
        print ("Just after saving to db user password is: ", user.password)
