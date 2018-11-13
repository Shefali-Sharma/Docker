from flask import Flask, render_template, request
import sys
import os
app = Flask(__name__)

@app.route('/')
def home():
    try:
        return render_template('home.html', pubs_created = '')
    except:
        return render_template('home.html', pubs_created = '')

@app.route('/about')
def about():
    return render_template('about.html', pubs_created = '')

@app.route('/contact') 
def contact():
    return render_template('contact.html', pubs_created = '')

@app.route('/publish', methods=['POST', 'GET'])
def publish():
    try:
        topicSelected = request.form['input']
        print(topicSelected)
        return render_template('home.html', pubs_created = 'New Publisher created.')
    except:
        return render_template('home.html', pubs_created = 'New Publisher created.')

@app.route('/notify', methods=['POST', 'GET'])
def notify():
    return render_template('home.html', pubs_created = '', notified = 'Subscribers Notified.')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4008, debug = True)
