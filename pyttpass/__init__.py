from flask import Flask

from config import Config
from pyttpass.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from pyttpass.main import bp as main_bp
    app.register_blueprint(main_bp)

    from pyttpass.passwords import bp as passwd_bp
    app.register_blueprint(passwd_bp, url_prefix='/passwords')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app