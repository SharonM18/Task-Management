from bson.objectid import ObjectId
from .. import mongo  # Ensure mongo is properly imported

class Uadmin:
    def find_user(username):
        return mongo.db.users.find_one(username)  # Adjust 'users' if needed


    def insert_user(user_data):
        result = mongo.db.users.insert_one(user_data)  # Adjust 'users' if needed
        return result

    
    def create_user(user_data):
        # Insert the user data into the database
        result = Uadmin.insert_user(user_data)
        return result.inserted_id  # Return the inserted ID

    
    def get_user_by_email(email):
        return Uadmin.find_user({'email': email})


    def get_user_by_id(user_id):
        if not ObjectId.is_valid(user_id):
            raise Exception('Invalid user ID')
        return Uadmin.find_user({'_id': ObjectId(user_id)})


# from werkzeug.security import generate_password_hash, check_password_hash
# from .. import mongo


# class Admin:
    
   
#     def create_admin(data):
#         # Check if the email already exists
#         if mongo.db.user.find_one({"email": data["email"]}):
#             return None
#         admin_id = mongo.db.user.insert_one(data).inserted_id
#         return str(admin_id)
    
   
#     def get_admin_by_email(email):
#         return mongo.db.user.find_one({"email": email})