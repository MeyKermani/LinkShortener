from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
from decouple import config
""" Creating app, api and db in order to prepare the system resources"""
app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))
api = Api(app)
db = SQLAlchemy(app)
import routes
migrate = Migrate(app, db)
if __name__ == '__main__':
    """ Runs the website """
    app.run()
