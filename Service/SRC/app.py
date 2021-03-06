from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello !</h3>" \
           "<h3>Welcome to Edison HealthLink.</h3>"

    return html.format()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
