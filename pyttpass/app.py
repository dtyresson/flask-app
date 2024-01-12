from flask import Flask, render_template
from config import Config
import os


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['VERSION'] = os.environ.get('VERSION')

    # Initialize Flask extensions here
    from pyttpass.extensions import db
    from pyttpass.models import User, Password
    db.init_app(app)
    with app.app_context():
        db.create_all()

    from flask_bootstrap import Bootstrap
    Bootstrap(app)

    from flask_login import LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    # Register blueprints here
    from pyttpass.main import main_bp
    app.register_blueprint(main_bp)

    from pyttpass.passwords import password_bp
    app.register_blueprint(password_bp, url_prefix='/passwords')

    from pyttpass.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    # Define a context processor to make the footer information available to all templates
    @app.context_processor
    def inject_version_info():
        return dict(version=app.config['VERSION'])

    return app