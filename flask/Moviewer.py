from flask import Flask
from flask import request
import sqlite3


app = Flask(__name__)

app.debug = True

@app.route("/")

def hello():
    return "Hello world"

@app.route("/hello/<name>")
def hello_to(name):
    return "Hello,{}!".format(name)

@app.route("/hello")
def hello_to_get_param():
    name = request.args.get("name")
    return "Hello, {}!!".format(name)

def get_db_con() -> sqlite3.connect:
    return sqlite3.connect("sql/db.sqlite")



if __name__ == "__main__":
    app.run()


