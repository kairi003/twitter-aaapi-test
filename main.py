import os
import base64
import hashlib
import hmac
import json

from flask import Flask, request, jsonify, make_response

app = Flask(__name__)
API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']


@app.route('/')
def top():
    return 'hello'


@app.route('/webhook', methods=['GET'], strict_slashes=False)
def webhook_challenge():
    crc_token = request.args.get('crc_token', '')
    digest = hmac.new(API_SECRET.encode(), crc_token.encode(), hashlib.sha256).digest()
    content = {'response_token': 'sha256=' + base64.b64encode(digest).decode()}
    return jsonify(content), 200

@app.route('/webhook', methods=['POST'], strict_slashes=False)
def webhook():
    response = make_response('', 200)
    response.mimetype = "text/plain"
    return response

app.run(port=8000)
