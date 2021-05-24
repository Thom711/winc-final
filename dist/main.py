from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/home')
def home():
    return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html', title="About")    


# Add some simple pages, add simple testing