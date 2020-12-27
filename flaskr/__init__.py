#imports
from flask import Flask, request, abort, json, jsonify
from models import setup_db, Publisher

#variables

#app
app = Flask(__name__)
setup_db(app)

#cors



@app.route('/')
def hello():
    return jsonify({
        'message': 'Hello World!'
    })

@app.route('/publisher', methods=['POST'])
def addPublisher():

    return 'Hello'

