from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("application.config.Config")
db = SQLAlchemy(app)

from application import routes
