from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world! Welcome to Digital Ocean! We are restarting now!'

@app.route('/cow')
def cow():
    return 'MOoooOo!'