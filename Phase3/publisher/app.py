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

@app.route('/add_publisher')
def add_publisher():
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

    sql = "INSERT INTO publisher (name, topic) VALUES (%s, %s)"
#   topic should be taken from user input
    newPub = test.publisher_generator(pub_sub_system)
    val = (newPub, "FASHION")
    cursor.execute(sql, val)
    cursor.execute('SELECT * FROM publisher')
    results = [{name: color} for (name, topic) in cursor]
    cursor.close()
    connection.commit()
    connection.close()

@app.route('/publish_and_notify')
def publish_and_notify():
# get topic from UI
#once topic is recevied, event should be sent to broker or subscriber

if __name__ == '__main__':
    pub_sub_system = PubSub.PubSubSystem()
    test = PubSub.Test()
    app.run(host="0.0.0.0", port=4002, debug = True)
