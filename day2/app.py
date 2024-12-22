from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello():
    return "<h1>Hello, World!</h1>"
