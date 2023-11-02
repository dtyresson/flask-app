from flask import Flask
import passwords


if __name__ == '__main__':


    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"