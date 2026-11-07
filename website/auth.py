from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/home')
def logout():
    return "<p>Home</p>"

@auth.route('/checker')
def sign_up():
    return "<p>Checker</p>"

@auth.route('/savedpasswords')
def saved_passwords():
    return "<p>Saved Passwords<p>"

@auth.route('/Help')
def help():
    return "<p>Help<p>"

