from flask import Flask, render_template, url_for, request
from markupsafe import escape
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'dev',
)

@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')

# Custom Function
@app.add_template_global
def repeat(s, n):
    return s * n 

# Making rutes
# Custom Filters
@app.route('/')
def index():
    name = 'Erik'
    friends = ['Alex','Paola','Juan','Jose']
    date = datetime.now()
    return render_template('index.html', 
                           name = name, 
                           friends = friends, 
                           date = date,)

# Rutes with parameters
# This route recive and string
@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
@app.route('/hello/<name>/<int:age>/<email>')
def hello(name = None, age = None, email = None):
    data = {
        'name' : name,
        'age' : age,
        'email' : email,
    }
    return render_template('hello.html', data = data)


@app.route('/code/<path:code>')
def codes(code):
    return f'<code>{escape(code)}</code>'


class RegisterForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=6, max=40)])
    submit = SubmitField('Register')

@app.route('/auth/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return f'Username: {username} - Password: {password}'
        
    # if request.method == 'POST':
    #     username = request.form.get('username')
    #     password = request.form.get('password')
        
    #     if len(username) >= 4 and len(username) <= 25 and len(password) >= 6 and len(password) <= 40:
    #         return f'Username: {username} - Password: {password}'
    #     else:
    #         error = 'Username must be 4 characters and Password must be 6 characters'
    #         return render_template('auth/register.html', form = form ,error = error)
    return render_template('auth/register.html', form = form)