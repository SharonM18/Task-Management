from werkzeug.security import generate_password_hash, check_password_hash
from .. import mongo

class Newuser:
    
    def create_user(data):
        # Check if the email already exists
        if mongo.db.user.find_one({"email": data["email"]}):
            return None
        data["password"] = generate_password_hash(data["password"])
        user_id = mongo.db.user.insert_one(data).inserted_id
        return str(user_id)
    
    
    def get_user_by_email(email):
        return mongo.db.user.find_one({"email": email})

