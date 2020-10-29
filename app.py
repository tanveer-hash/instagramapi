import flask
from flask_restful import Api, Resource, reqparse, request
import requests
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def get_data():
    un = request.args.get('username', type = str)
    url = "https://www.instagram.com/"+"{0}".format(un) + "/?__a=1"
    return requests.get(url).content
app.run()