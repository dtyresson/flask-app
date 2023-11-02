from flask import render_template
from pyttpass.passwords import bp

@bp.route('/')
def index():
    return render_template('passwords/index.html')

@bp.route('/passwords/')
def passwords():
    return render_template('passwords/passwords.html')