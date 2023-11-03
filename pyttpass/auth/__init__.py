from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

from pyttpass.auth import routes