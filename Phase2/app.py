from flask import Flask, render_template, request
import sys
import os
app = Flask(__name__)

@app.route('/')
def home():
    try:
        return render_template('home.html', topicsList = [])
    except:
        return render_template('home.html', topicsList = [])

@app.route('/about')
def about():
    return render_template('about.html', topicsList = [])

@app.route('/contact')
def contact():
    return render_template('contact.html', topicsList = [])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4001, debug = True)
