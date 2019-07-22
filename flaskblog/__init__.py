from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskblog import routes

app = Flask(__name__)

app.config['SECRET_KEY'] = '47cece3f2555fc43ba70ef78cdf4321a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

