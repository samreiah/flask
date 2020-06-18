import os
from flask import Blueprint, current_app

from app.controllers.home_controller import index as home_index

from app.controllers.authentication_controller import getLogin

routes = Blueprint('routes', __name__)
routes.add_url_rule('/', view_func=home_index, methods=['GET'])

# Auth Routes
routes.add_url_rule('/login', view_func=getLogin, methods=['GET', 'POST'])
