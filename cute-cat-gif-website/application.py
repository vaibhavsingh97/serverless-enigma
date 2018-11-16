import os
import json
from random import randint
import giphy_client
from flask import Flask
from giphy_client.rest import ApiException

app = Flask(__name__)

api_instance = giphy_client.DefaultApi()
API_KEY = os.environ.get('GIPHY_TOKEN')
q = 'cat'
limit = 100
offset = 0
rating = 'g'
lang = 'en'
fmt = 'json'


@app.route("/")
def home():
    return json.dumps({
        'status code': 200,
        'message': "Welcome to cat gif API"
    })


@app.route("/catgif")
def get_cat_gif():
    try:
        api_response = api_instance.gifs_search_get(
            API_KEY, q, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt).to_dict()
        random_gif = api_response['data'][randint(
            0, 100)]['images']['downsized']['url']
        return json.dumps({
            'status_code': 200,
            'url': random_gif
        })
    except ApiException as e:
        return json.dumps({
            'status code': 400,
            'message': "Exception when calling giphy api: {}".format(e)
        })
