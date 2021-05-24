from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world! Welcome to Github!'

@app.route('/cow')
def cow():
    return 'MOoooOo!'