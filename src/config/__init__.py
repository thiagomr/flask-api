import os
from flask_sqlalchemy import SQLAlchemy


class Config:
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '5432')
    DB_USER = os.environ.get('DB_USER', 'postgres')
    DB_PASS = os.environ.get('DB_PASS', 'admin')
    DB_NAME = os.environ.get('DB_NAME', 'api')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL', 'postgresql://%s:%s@%s:%s/%s' % (DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


db = SQLAlchemy()
settings = Config()
