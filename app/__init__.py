import flask
from flask_pymongo import PyMongo

app = flask.Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:2717/new_york"
mongo = PyMongo(app)