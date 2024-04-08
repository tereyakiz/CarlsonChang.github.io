from flask import render_template, request, redirect, url_for, session
from app import app

# Define routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'your_username' and password == 'your_password':
            session['logged_in'] = True
            return redirect(url_for('profile'))
        else:
            return 'Invalid username or password'
    # Render login form template for GET requests
    return render_template('login.html')

@app.route('/profile')
def profile():
    if session.get('logged_in'):
        return 'Welcome to your profile!'
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))