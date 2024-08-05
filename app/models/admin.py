from werkzeug.security import generate_password_hash, check_password_hash
from .. import mongo

class Admin:
    
   
    def create_admin(data):
        # Check if the email already exists
        if mongo.db.user.find_one({"email": data["email"]}):
            return None
        admin_id = mongo.db.user.insert_one(data).inserted_id
        return str(admin_id)
    
   
    def get_admin_by_email(email):
        return mongo.db.user.find_one({"email": email})