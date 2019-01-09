from flask import Flask, render_template, request
import sys
import os
import time
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    newRes = 'Hello World! I have been seen ' + str(count) + ' times!'
    return render_template('home.html', myResult=newRes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    