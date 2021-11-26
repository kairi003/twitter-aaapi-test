import re
import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def top():
  return 'hello'

@app.route('/twitter/webhook', methods=['GET', 'POST'])
def webhook():
    return 'Hello'

app.run(port=8000)