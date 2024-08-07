from flask import Blueprint
from ..controllers import admin_controller

app = Blueprint ('admin',__name__)

app.route("/signup_admin", methods=["POST", "GET"]) (admin_controller.signup_admin)
app.route("/login", methods=["POST", "GET"])(admin_controller.login)