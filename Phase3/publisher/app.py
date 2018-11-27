from flask import Flask, render_template, request
import sys
import os
import PubSub
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
        # topicSelected = request.form['input']
        # config = {
        # 'user': 'root',
        # 'password': 'root',
        # 'host': 'db',
        # 'port': '3306',
        # 'database': 'knights'
        # }
        # connection = mysql.connector.connect(**config)
        # cursor = connection.cursor()
        # cursor = connection.cursor(buffered=True)

        # sql = "INSERT INTO publisher (name, topic) VALUES (%s, %s)"
        # #   topic should be taken from user input
        # newPub = test.publisher_generator(pub_sub_system)
        # val = (newPub, topicSelected)
        # cursor.execute(sql, val)
        # cursor.execute('SELECT * FROM publisher')
        # results = [{name: color} for (name, topic) in cursor]
        # cursor.close()
        # connection.commit()
        # connection.close()
        print("shefali")
        return render_template('home.html', pubs_created = 'New Publisher created.')
    except:
        print("here")
        return render_template('home.html', pubs_created = 'New Publisher created.')

@app.route('/notify', methods=['POST', 'GET'])
def notify():
    # url = "http://0.0.0.0:4002/"
    #    url = "localhost:5002/"
    #    request = urllib.request.Request(url)
    #    response = urllib.request.urlopen(request)
    #    data = response.read().decode('utf-8')
    #    parsed_json = json.loads(data)
    #    topics = parsed_json["topics"]
#    resp = requests.get('http://0.0.0.0:5002')
#    print('Response from TestRequest: '+resp.text)
    return render_template('home.html', pubs_created = '', notified = 'Subscribers Notified.')

if __name__ == '__main__':
    pub_sub_system = PubSub.PubSubSystem()
    test = PubSub.Test()
    app.run(host="0.0.0.0", port=4010, debug = True)
