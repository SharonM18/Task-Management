from bson.objectid import ObjectId
from .. import mongo 

from app import mongo

class admin_user:
    def __init__(self, email, name, surname, password, role):
        self.email = email
        self.name = name
        self.surname = surname
        self.password = password
        self.role = role

    def save(self):
        mongo.db.users.insert_one({
            "email": self.email,
            "name": self.name,
            "surname": self.surname,
            "password": self.password,
            "role": self.role
        })

    @staticmethod
    def find_by_email(email):
        user_data = mongo.db.users.find_one({"email": email})
        if user_data:
            return admin_user(
                email=user_data['email'],
                name=user_data['name'],
                surname=user_data['surname'],
                password=user_data['password'],
                role=user_data['role']
            )
        return None