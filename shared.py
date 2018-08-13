import os
import random

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from customjsonencoder import CustomJSONEncoder

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = "./uploads"
app.config["THUMB_FOLDER"] = os.path.join(app.config["UPLOAD_FOLDER"], "thumb")
app.json_encoder = CustomJSONEncoder
db = SQLAlchemy(app)
rest_api = Api(app)


def get_secret():
    return open("secret").read()


app.secret_key = get_secret()


def gen_poster_id():
    id_chars = "ABCDEF0123456789"
    return ''.join(random.sample(id_chars, 4))
