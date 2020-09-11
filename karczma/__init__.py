from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from karczma import options
from flask_login import LoginManager

app=Flask(__name__)
app.config.from_object(options.Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
login = LoginManager(app)

from karczma import views

