from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from ..models.admin import admin_user

def signup():
    if request.method == 'POST':
        email = request.json.get('email')
        name = request.json.get('name')
        surname = request.json.get('surname')
        password = request.json.get('password')
        role = request.json.get('role', 'user') 

        # Set the default role to 'user'
        role = request.json.get('role', 'user')

        # Check if the user already exists
        if admin_user.find_by_email(email):
            return jsonify({"msg": "User already exists"}), 409

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Create a new user
        new_user = admin_user(email=email,name=name,surname=surname,password=hashed_password,role=role)
        new_user.save()

        return jsonify({"msg": "User registered successfully"}), 201
    else:
        return jsonify({"msg": "Invalid request method"}), 405


def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = admin_user.find_by_email(email)
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity={"email": user.email, "role": user.role})
        return jsonify({"access token": access_token ,"role": user.role} ), 200

    return jsonify({"msg": "Invalid credentials"}), 401