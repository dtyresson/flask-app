from flask import Blueprint

bp = Blueprint('main', __name__)

from pyttpass.main import routes