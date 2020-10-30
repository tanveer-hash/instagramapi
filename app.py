import flask
from flask_restful import Api, Resource, reqparse, request
import requests
app = flask.Flask(__name__)
app.run(host='157.39.200.88', port=5001)
@app.route('/', methods=['GET'])
def get_data():
    return "Hello World"
app.run()
