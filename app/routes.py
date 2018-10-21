from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Patrick'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'So glad we now have a great community around this legacy DB!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The AS/400 is so cool, can we make this a one stop shop for all things AS/400!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for user{}, remember_me{}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
