import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
    'username',
        type = str,
        required = True,
        help = "This field cannot be left blank"
    )
    parser.add_argument(
    'password',
        type = str,
        required = True,
        help = "This field cannot be left blank"
    )

    def post(self):

        print ("Trying to create user")
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):

            return {"message": "User already exists"}, 400

        user = UserModel(**data)

        user.save_user_to_db()

        return {"message": "User Created Successfully"}, 201

class Showusers(Resource):

    def get(self):

        ret_user = []
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        all_user_query = "SELECT * FROM users"
        users = cursor.execute(all_user_query)
        for user in users:
            ret_user.append(user)
        connection.commit()
        connection.close()
        return {"users":ret_user}
