from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager
from ..models.admin import UserAdmin
from datetime import datetime, timedelta
import os
import jwt


def signup_admin(username, password, email):
    
    user_data = {
        'name': username,
        'email': email,
        'password': password,
        'role': 'admin'
    }
    result = UserAdmin.create_user(user_data)
    return result

def signup_user(username, password, email):
    
    user_data = {
        'name': username,
        'email': email,
        'password': password,
        'role': 'user'
    }
    result = UserAdmin.create_user(user_data)
    return result

def signup():
    
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    role = request.json.get('role')

    if not username or not email or not password or not role:
        return jsonify({
            'message': 'Username, email, password, and role are required',
            'username': username,
            'email': email
        }), 400

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    if role == 'admin':
        user_id = register_admin(username, hashed_password, email)
    else:
        user_id = register_user(username, hashed_password, email)

    payload = {
        'user_id': user_id,
        'role': role,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, os.environ.get('SECRET_KEY'), algorithm='HS256')

    return jsonify({'token': token.decode('utf-8')}), 201

def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = UserAdmin.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        
        payload = {
            'user_id': user.id,
            'role': user.role,
            'exp': datetime.utcnow() + timedelta(hours=1)
        }
        token = jwt.encode(payload, os.environ.get('SECRET_KEY'), algorithm='HS256')

        return jsonify({'token': token.decode('utf-8')}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

def register_admin(username, password, email):
    return 1

def register_user(username, password, email):
    return 2

# def signup_admin():
#     name = request.json.get('name')
#     surname = request.json.get('surname')
#     email = request.json.get('email')
#     password = request.json.get('password')

#     if not all([name, surname, email, password]):
#         return jsonify({"error": "All fields are required"}), 400

#     hashed_password = generate_password_hash(password)
#     user = {"name": name, "surname": surname, "email": email, "password": hashed_password}
    
#     if Admin.create_admin(user):
#         return jsonify({"message": "User created successfully", "redirect": url_for('user.login')}), 201
#     else:
#         return jsonify({"error": "User creation failed"}), 500

# def login_admin():
#     email = request.json.get('email')
#     password = request.json.get('password')

#     if not all([email, password]):
#         return jsonify({"error": "Email and password are required"}), 400

#     user = Admin.get_user_by_email(email)
    
#     if user and check_password_hash(user['password'], password):
#         # Assuming session management is done here, and user_id is stored in the session
#         session['user_id'] = str(user['_id'])
#         return jsonify({"message": "Login successful"}), 200
#     else:
#         return jsonify({"error": "Invalid email or password"}), 401