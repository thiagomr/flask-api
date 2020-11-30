from dotenv import load_dotenv, find_dotenv
from connexion import FlaskApp
from flask_migrate import Migrate
from src.config import db, settings
from src.db import models

load_dotenv(find_dotenv())

flask = FlaskApp(__name__, specification_dir='src/config')
flask.add_api('swagger.yaml')

app = flask.app
app.config.from_object(settings)
app.app_context().push()

db.init_app(app)
Migrate(app, db)
