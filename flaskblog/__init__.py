from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '47cece3f2555fc43ba70ef78cdf4321a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://pzbscfjy:jXVhbgRds10K3BX2lJnJoQTenGmhYwc2@raja.db.elephantsql.com:5432/pzbscfjy'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes