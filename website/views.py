from flask import render_template, Blueprint, url_for

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")