import os
import base64
import hashlib
import hmac
import json

from flask import Flask, request

app = Flask(__name__)
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']

@app.route('/')
def top():
  return 'hello'

@app.route('/webhooks/twitter', methods=['GET', 'POST'])
def webhook():
    return 'Hello'

app.run(port=8000)