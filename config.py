import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    UPLOAD_FOLDER = os.path.join(basedir, 'app/static/uploads')
    SECRET_KEY = os.urandom(24).hex()  # os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SERVER_NAME = 'DeadFishProject'
    HOST = '0.0.0.0'
    # PORT = 8000
