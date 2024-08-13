from flask import Blueprint
from ..controllers import admin_controller

app = Blueprint ('admin',__name__)

app.route("/signup", methods=["POST"]) (admin_controller.signup)
app.route("/login", methods=["POST"])(admin_controller.login)