from flask import Blueprint

bp = Blueprint('passwords', __name__)


from pyttpass.passwords import routes