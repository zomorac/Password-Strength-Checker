from flask import Blueprint, render_template #seperatesapp  out,split out, organized

views = Blueprint('views', __name__)

@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/checker')
def checker():
    return render_template("checker.html")

@views.route('/savedpasswords')
def saved_passwords():
    return render_template("saved_passwords.html")

@views.route('/help')
def help_page():
    return render_template("help.html")


