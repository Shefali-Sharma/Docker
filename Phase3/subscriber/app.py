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
        config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'knights'
        }
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor = connection.cursor(buffered=True)

        sql = "INSERT INTO subscriber (topic, name) VALUES (%s, %s)"
        #   topic should be taken from user input
        newSub = test.subscription_generator(pub_sub_system)
        val = (topicSelected,newSub)
        cursor.execute(sql, val)
        cursor.execute('SELECT * FROM subscriber')
        results = [{name: color} for (topic, name) in cursor]
        cursor.close()
        connection.commit()
        connection.close()
        print(topicSelected)
        return render_template('home.html', subs_created = 'New Subscriber created.', pubSubsList=['No Notifications Received.'])
    except:
        return render_template('home.html', subs_created = 'New Subscriber created.', pubSubsList=['No Notifications Received.'])

def notify():
    return render_template('home.html', subs_created = '', pubSubsList=['Subscriber notified for FASHION.'])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4001, debug = True)
