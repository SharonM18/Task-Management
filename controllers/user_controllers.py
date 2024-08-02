from flask import Flask,  request, redirect, url_for, session, jsonify 
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from ..models.user import Newuser


def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        email = request.form.get('email')
        password = request.form.get('password')

        if not all([name, surname, email, password]):
           

         user = {"name": name, "surname": surname, "email": email, "password": password}
        if Newuser.create_user(user):
            return redirect(url_for('user.login'))
        
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Newuser.get_user_by_email(email)
        if user and check_password_hash(user['password'], password):
            return redirect(url_for('services_bp.add_service'))
        
