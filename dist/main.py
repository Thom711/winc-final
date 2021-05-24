from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '16! change'

@app.route('/cow')
def cow():
    return 'MOoooOo!'