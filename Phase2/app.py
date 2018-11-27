from flask import Flask, render_template, request
import PubSub
import sys
import os
app = Flask(__name__)

@app.route('/')
def home():
    try:
        return render_template('home.html', pubSubsList = [], subs_created = "")
    except:
        return render_template('home.html', pubSubsList = [], subs_created = "")

@app.route('/subscribe', methods=['POST', 'GET'])
def subscribe():
    newSub = test.subscription_generator(pub_sub_system)
    # pub_sub_system.print_pub_sub_system()
    return render_template('home.html', subs_created = newSub, pubSubsList = [])

@app.route('/publish', methods=['POST', 'GET'])
def publish():
    newPub = test.publisher_generator(pub_sub_system)
    # print(newPub)
    return render_template('home.html', pubs_created = newPub, pubSubsList = [])

@app.route('/notify', methods=['POST', 'GET'])
def notify():
    try:
        res = test.notify(pub_sub_system)
        return render_template('home.html', pubSubsList = res)
    except:
        return render_template('home.html', subs_created = "")

@app.route('/about')
def about():
    return render_template('about.html', pubSubsList = [])

@app.route('/contact') 
def contact():
    return render_template('contact.html', pubSubsList = [])

if __name__ == '__main__':
    pub_sub_system = PubSub.PubSubSystem()
    test = PubSub.Test()
    app.run(host="0.0.0.0", port=4020, debug = True)
