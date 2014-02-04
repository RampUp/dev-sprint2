# This is whre you can start you python file for your week1 web app
# Name: Christopher Van Schyndel

import flask, flask.views
import os
import functools
app = flask.Flask(__name__)
# Dun do dat
app.secret_key = "bagel"

users = {'Chris':'bagel'}

class Main(flask.views.MethodView):
	def get(self):
		return flask.render_template('index.html')
	
	def post(self):
		if 'logout' in flask.request.form:
			flask.session.pop('username', None)
			return flask.redirect(flask.url_for('index'))
		required = ['username', 'passwd']
		for r in required:
			if r not in flask.request.form:
				flask.flash("Error: {0} is required.".format(r))
				return flask.redirect(flask.url_for('index'))
		username = flask.request.form['username']
		passwd = flask.request.form['passwd']
		if username in users and users[username] == passwd:
			flask.session['username'] = username
		else:
			flask.flash("Username doesn't exist or incorrect password.")
		return flask.redirect(flask.url_for('index'))

def login_required(method):
	@functools.wraps(method)
	def wrapper(*args, **kwargs):
		if 'username' in flask.session:
			return method(*args, **kwargs)
		else:
			flask.flash("A login is required to see the page!")
			return flask.redirect(flask.url_for('index'))
	return wrapper

class Remote(flask.views.MethodView):
	@login_required
	def get(self):
		return flask.render_template('remote.html')

	@login_required
	def post(self):
		result = eval(flask.request.form['expression'])
		flask.flash(result)
		return flask.redirect(flask.url_for('remote'))

def is_triangle(a, b, c):
	if a > b + c or b > a + c or c > a + b:
		return 'no, a triangle is not possible.'
	else:
		return 'yes, a triangle is possible.'

def stickinput(a, b, c):
	if a.isdigit() == False or b.isdigit() == False or c.isdigit() == False:
		return 'None'
	else:
		a = int(a)
		b = int(b)
		c = int(c)
		return is_triangle(a, b, c)

class Triangle(flask.views.MethodView):
	@login_required
	def get(self):
		return flask.render_template('triangle.html')
	
	@login_required
	def post(self):
		result = 'With the sides given: '
		result += str((flask.request.form['expressionA'])) + ', ' + str((flask.request.form['expressionB'])) + ', and ' + str((flask.request.form['expressionC'])) + '. '
		a = str((flask.request.form['expressionA']))
		b = str((flask.request.form['expressionB']))
		c = str((flask.request.form['expressionC']))
		trianglechecked = stickinput(a, b, c)
		result += 'Then ' + trianglechecked
		if a.isdigit() == True and b.isdigit() == True and c.isdigit() == True:
			flask.flash(result)
		return flask.redirect(flask.url_for('triangle'))

class Music(flask.views.MethodView):
	@login_required
	def get(self):
		songs = os.listdir('static/music/')
		return flask.render_template('music.html', songs = songs)

class Asteroids(flask.views.MethodView):
	@login_required
	def get(self):
		return flask.render_template('asteroids.html')

class RemoteZsnes(flask.views.MethodView):
	@login_required
	def get(self):
		return flask.render_template('remotezsnes.html')

class CoffeeData(flask.views.MethodView):
	@login_required
	def get(self):
		return flask.render_template('coffeedata.html')

app.add_url_rule('/',
				 view_func=Main.as_view('index'),
				 methods=["GET", "POST"])
app.add_url_rule('/remote/',
				 view_func=Remote.as_view('remote'),
				 methods=["GET", "POST"])
app.add_url_rule('/triangle/', 
				 view_func=Triangle.as_view('triangle'),
				 methods=["GET", "POST"])
app.add_url_rule('/music/', 
				 view_func=Music.as_view('music'),
				 methods=["GET"])
app.add_url_rule('/asteroids/',
				 view_func=Asteroids.as_view('asteroids'),
				 methods=["GET"])
app.add_url_rule('/remotezsnes/',
				 view_func=RemoteZsnes.as_view('remotezsnes'),
				 methods=["GET"])
app.add_url_rule('/asteroids/',
				 view_func=CoffeeData.as_view('coffeedata'),
				 methods=["GET"])


app.debug = True
app.run()