from flask import Flask, render_template, request
import sys
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', topicsList = [])

@app.route('/callback', methods=['POST'])
def callback():
    src = request.form['srcCode']
    path = "/Users/shefali9222/Documents/GitHub/Docker/Phase1/compose/app.py"
    myfile = open(path, "w")
    myfile.write(src)
    myfile.close()
    os.system("sh /Users/shefali9222/Documents/GitHub/Docker/Phase1/compose/docker.sh")
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4002, debug = True)
