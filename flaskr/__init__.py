#imports
from flask import Flask

#variables

#app
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello!'