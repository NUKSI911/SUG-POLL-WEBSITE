from flask import Flask, redirect, render_template, abort, flash, url_for
from flask_login import LoginManager, UserMixin
from model import db

app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = ""

user = {
    'vote': False,
    'login': False
}

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('index.html', user=user)

@app.route('/login', methods=['POST'])
def login_route():
    user['login'] = True
    return redirect(url_for('homepage'))

@app.route('/create')
def create():
    db.create_all()
    return 'created'

@app.route('/vote', methods=['POST'])
def vote_route():
    return render_template('index.html')

@app.errorhandler(400)
def bad_request(err):
	return render_template("errors.html")

@app.errorhandler(401)
def un_authenticated(err):
	return render_template("errors.html")

@app.errorhandler(403)
def for_bidden(err):
	return render_template("errors.html")

@app.errorhandler(404)
def page_not_found(err):
	return render_template("errors.html")

@app.errorhandler(405)
def four_oh_five(err):
	return render_template("errors.html")

@app.errorhandler(406)
def not_acceptable(err):
	return render_template("errors.html", error = err)

if __name__ =='__main__':
	app.run(host="0.0.0.0",debug=True)