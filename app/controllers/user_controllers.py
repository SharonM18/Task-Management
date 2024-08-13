# from flask import Flask, request, url_for, session, jsonify
# from werkzeug.security import generate_password_hash, check_password_hash
# from bson.objectid import ObjectId
# from ..models.user import User

# def signup_user():
#     if request.method == 'POST':
#         name = request.json.get('name')
#         surname = request.json.get('surname')
#         email = request.json.get('email')
#         password = request.json.get('password')
#         role = request.json.get('role', 'user')  # Default role is 'user'

#         # Check if all required fields are provided
#         if not all([name, surname, email, password]):
#             return jsonify({"error": "All fields are required"}), 400

#         # Hash the password
#         hashed_password = generate_password_hash(password)

#         # Create a new user
#         user = {"name": name,"surname": surname,"email": email,"password": hashed_password,"role": role}

#         try:
#             # Save the user
#             User.create_user(user)
#             return jsonify({"message": "User created successfully"}), 201
#         except Exception as e:
#             # Handle any exceptions that may occur during user creation
#             return jsonify({"error": "User creation failed"}), 500
#     else:
#         return jsonify({"error": "Invalid request method"}), 405


# def login():
#     email = request.json.get('email')
#     password = request.json.get('password')

#     if not all([email, password]):
#         return jsonify({"error": "Email and password are required"}), 400

#     user = User.get_user_by_email(email)
    
#     if user and check_password_hash(user['password'], password):
#         session['user_id'] = str(user['_id'])
#         return jsonify({"message": "Login successful"}), 200
#     else:
#         return jsonify({"error": "Invalid email or password"}), 401

 
    
