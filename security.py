from models.user import UserModel
from werkzeug.security import safe_str_cmp

def authenticate(username, password):
    print (f"authenticating {username} and {password}")
    user = UserModel.find_by_username(username)
    print("In auth function")
    print (user.id)
    print (user.username)
    print (user.password)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload["identity"] #the token
    return UserModel.find_by_userid(user_id)
