from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

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

from market import routes 