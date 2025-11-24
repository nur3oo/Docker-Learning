from flask import Flask
import redis

app = Flask(__name__)


r = redis.Redis(host="redis", port=6379)

@app.route("/")
def hello_everyone():
    return "Hello Everyone"

@app.route("/count")
def count():
    visits = r.incr("visits")
    return f"This has been visited {visits} times before"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
