from datetime import datetime

from flask import Flask, jsonify, Response

from . import app, mongo

@app.route("/")
def home_page():
    x = mongo.db.restaurants.find_one()
    print(x)
  #   return jsonify({
  #   "01": {
  #     "note": "This data is very simple because we're demonstrating only the mechanism."
  #   }
  # })BSONObjectIdConverter
    return "toto"

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
