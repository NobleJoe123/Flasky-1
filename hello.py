from flask import Flask, make_response, render_template, session, redirect, url_for, flash
from flask import request
from flask import redirect
from flask import abort
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired




app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

# @app.route('/')
# def index():
#  return '<h1>Hello World!</h1>'

# @app.route('/user/<name>')
# def user(name):
#  return '<h1>Hello, %s!</h1>' % name

# @app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return '<p>Your browser is %s</p>' % user_agent

# @app.route('/')
# def index():
#  return '<h1>Bad Request</h1>', 400


# @app.route('/')
# def index():
#  response = make_response('<h1>This document carries a cookie!</h1>')
#  response.set_cookie('answer', '42')
#  return response

# @app.route('/')
# def index():
#  return redirect('http://www.example.com')


# @app.route('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return '<h1>Hello, %s</h1>' % user.name


# @app.route('/index')
# def index():
#  return render_template('index.html')
# @app.route('/user/<name>')
# def user(name):
#  return render_template('user.html', name=name)

# @app.errorhandler(404)
# def page_not_found(e):
#  return render_template('404.html'), 404

# @app.route('/')
# def index():
#  return render_template('index.html',
#  current_time=datetime.utcnow())
 
class NameForm(FlaskForm):
     name = StringField('What is your name?', validators=[DataRequired()])
     submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
         name = form.name.data
         form.name.data = ''
    return render_template('index.html', form=form, name=name)


# @app.route('/', methods=['GET', 'POST'])
# def index():
#  form = NameForm()
#  if form.validate_on_submit():
#      session['name'] = form.name.data
#      return redirect(url_for('index'))
#  return render_template('index.html', form=form, name=session.get('name'))

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         old_name = session.get('name')
#         if old_name is not None and old_name != form.name.data:
#             flash('Looks like you have changed your name!')
#             session['name'] = form.name.data
#             form.name.data = ''
#             return redirect(url_for('index'))
#         return render_template('index.html',
#                                form = form, name = session.get('name'))


if __name__ == '__main__':
 app.run(debug=True)
