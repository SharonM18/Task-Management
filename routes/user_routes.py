from flask import Blueprint
from ..controllers import user_controllers

app = Blueprint ('user',__name__)

app.route("/signup", methods=["POST", "GET"]) (user_controllers.signup_user)
app.route("/login", methods=["POST", "GET"])(user_controllers.login)
