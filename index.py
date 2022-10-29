from flask import Flask, render_template

app = Flask(__name__)

# Running
# set FLASK_APP=index.py
# set FLASK_APP=

# @app.route("/")
# def hello_world():
#     return "<h1>Hello new text<h1>"

# @app.route('/about/<username>')
# def about_page(username):
#     return f'<h1>This is the about page of {username}<h1>'

@app.route("/")
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    return render_template('market.html', item_name='Phone')