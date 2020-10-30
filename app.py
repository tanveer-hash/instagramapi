import flask
from flask_restful import Api, Resource, reqparse, request
import requests
app = flask.Flask(__name__)
import os
port = int(os.environ.get('PORT', 5000))
app.run(port=port, debug=True)
@app.route('/', methods=['GET'])
def get_data():
    return "Hello World"
app.run()
