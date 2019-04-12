import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


app = Flask(__name__)
bcrypt=Bcrypt(app)
app.secret_key="\x88N\xf5]\xf8\xe9\xf4\xcc#\x11\xf4\x9dz\x1f3"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///QuindittyArt.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

ROOT_DIR = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.join(ROOT_DIR, 'client', 'templates')
STATIC_DIR = os.path.join(ROOT_DIR, 'client', 'static')
IMAGE_DIR = os.path.join(ROOT_DIR, 'client', 'static', 'images')

app.config['UPLOAD_FOLDER'] = IMAGE_DIR

app.template_folder = TEMPLATES_DIR
app.static_folder = STATIC_DIR
app.image_folder = IMAGE_DIR

db = SQLAlchemy(app)
migrate = Migrate(app, db)