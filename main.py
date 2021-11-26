import base64
import hashlib
import hmac
import json

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def top():
  return 'hello'

@app.route('/webhooks/t', methods=['GET', 'POST'])
def webhook():
    return 'Hello'

app.run(port=8000)