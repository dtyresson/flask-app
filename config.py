import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    # TODO: Improve loading of env
    try:
        from dotenv import load_dotenv
        load_dotenv()
        SECRET_KEY = os.getenv('SECRET_KEY')
    except Exception as e:
        print(f'Could not load Secret key from file: {e}')
        SECRET_KEY = os.environ.get('SECRET_KEY')
    finally:
        if not SECRET_KEY:
            raise Exception('No Secret Key provided.')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'pyttpass.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False