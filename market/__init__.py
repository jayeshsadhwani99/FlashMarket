from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Initialize app
app = Flask(__name__)

# Configure the Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# Initialize Database
db = SQLAlchemy(app)

# This key is required by the form to connect to the Database
app.config['SECRET_KEY'] = '94ac5a795d5f5736e19c3ebe'

# Create an instance of Bcrypt
bcrypt = Bcrypt(app)

# Initialize the Login Manager
login_manager = LoginManager(app)

# Tell the login manager about the login page
login_manager.login_view = 'login'

# Customize Flash Message
login_manager.login_message_category = 'info'

from market import routes 