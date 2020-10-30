import flask
from flask_restful import Api, Resource, reqparse, request
import requests
app = flask.Flask(__name__)
app.run(debug=True, port=33507)
@app.route('/', methods=['GET'])
def get_data():
    return "Hello World"
app.run()
