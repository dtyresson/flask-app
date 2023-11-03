from flask import Blueprint

password_bp = Blueprint('passwords', __name__)


from pyttpass.passwords import routes