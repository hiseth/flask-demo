from flask import Blueprint, render_template
from .extension import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    # return 'Index'
    return render_template('index.html')


@main.route('/profile')
def profile():
    # return 'Profile'
    return render_template('profile.html')