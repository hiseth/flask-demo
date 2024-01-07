from flask import Blueprint, render_template
from .extension import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    # return 'Login'
    return render_template('login.html')

@auth.route('/signup')
def singup():
    # return 'Singup'
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    # return 'Logout'
    return render_template('logout.html')