from flask import Flask, render_template
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    req = requests.get('https://cat-fact.herokuapp.com/facts')
    return req.content

if __name__ == "__main__":
   app.run(port=8080, debug=True)

# Set-ExecutionPolicy Unrestricted -Scope Process