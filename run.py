from flask import Flask, render_template
import requests
from config import API_KEY
from dotenv import load_dotenv


# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    # This will render the index.html template from the templates folder
    return render_template('index.html')
@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/feed')
def feed():
    return render_template('feed.html')

@app.route('/notification')
def notification():
    return render_template('notification.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

# Run the Flask application
if __name__ == '__main__':
    # Enabling debugger for development purposes
    app.run(debug=True, host='0.0.0.0', port=8080)

