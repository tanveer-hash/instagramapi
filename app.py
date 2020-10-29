import flask
from flask_restful import Api, Resource, reqparse, request
import requests
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def get_data():
    return "Hello World"
app.run()
