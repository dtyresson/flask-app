from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

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

    return app