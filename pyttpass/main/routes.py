from flask import render_template
from pyttpass.main import bp

@bp.route('/')
def index():
    return render_template('index.html')
