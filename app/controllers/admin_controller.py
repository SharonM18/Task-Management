from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os
import jwt
from ..models.admin import Uadmin

auth_bp = Blueprint('auth', __name__)

def signup_admin(name, password, email):
    user_data = {
        'name': name,
        'email': email,
        'password': password,
        'role': 'admin'
    }
    return Uadmin.create_user(user_data)

def signup_user(name, password, email):
    user_data = {
        'name': name,
        'email': email,
        'password': password,
        'role': 'user'
    }
    return Uadmin.create_user(user_data)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')
    role = request.json.get('role')

    if not name or not email or not password or not role:
        return jsonify({
            'message': 'name, email, password, and role are required',
            'name': name,
            'email': email
        }), 400

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    if role == 'admin':
        user_id = signup_admin(name, hashed_password, email)
    else:
        user_id = signup_user(name, hashed_password, email)

    if not user_id:
        return jsonify({'message': 'User creation failed. Email might already exist.'}), 400

    payload = {
        'user_id': user_id,
        'role': role,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, os.environ.get('SECRET_KEY'), algorithm='HS256')

    return jsonify({'token': token}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = Uadmin.get_user_by_email(email)

    if user and check_password_hash(user['password'], password):
        payload = {
            'user_id': str(user['_id']),
            'role': user['role'],
            'exp': datetime.utcnow() + timedelta(hours=1)
        }
        token = jwt.encode(payload, os.environ.get('SECRET_KEY'), algorithm='HS256')

        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Invalid email or password'}), 401

