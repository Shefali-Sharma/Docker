from flask import Flask, render_template, request
import sys
import os
app = Flask(__name__)

@app.route('/')
def home():
    try:
        return render_template('home.html', subs_created = '', pubSubsList=['No Notifications Received.'])
    except:
        return render_template('home.html', subs_created = '', pubSubsList=['No Notifications Received.'])

@app.route('/about')
def about():
    return render_template('about.html', subs_created = '', pubSubsList=['No Notifications Received.'])

@app.route('/contact') 
def contact():
    return render_template('contact.html', subs_created = '', pubSubsList=['No Notifications Received.'])

@app.route('/subscribe', methods=['POST', 'GET'])
def subscribe():
    try:
        topicSelected = request.form['input']
        print(topicSelected)
        return render_template('home.html', subs_created = 'New Subscriber created.', pubSubsList=['No Notifications Received.'])
    except:
        return render_template('home.html', subs_created = 'New Subscriber created.', pubSubsList=['No Notifications Received.'])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4008, debug = True)
