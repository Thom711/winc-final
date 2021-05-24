from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Woooooo'

@app.route('/cow')
def cow():
    return 'MOoooOo!'


# Add some simple pages, add testing. Make the deploy script fail if testing is not passed