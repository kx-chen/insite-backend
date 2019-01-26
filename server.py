# Imports
from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> hi </h1>'


@app.route('/summarize', methods=['POST'])
def summarize():
    pass


if __name__ == '__main__':
    app.run()
