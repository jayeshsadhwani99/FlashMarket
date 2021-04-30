from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize app
app = Flask(__name__)

# Configure the Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# Initialize Database
db = SQLAlchemy(app)

from market import routes 