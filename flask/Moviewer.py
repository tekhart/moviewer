from flask import Flask
from flask import request
import json
import sqlite3

app = Flask(__name__)

app.debug = True

def get_db_con() -> sqlite3.connect:
    return sqlite3.connect("sql/db.sqlite")

@app.route("/")

def hello():
    with get_db_con() as con:
        cur = con.cursor()

        q = "select * from rotten"
        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json

@app.route("/hello/<name>")
def hello_to(name):
    return "Hello,{}!".format(name)

@app.route("/hello")
def hello_to_get_param():
    name = request.args.get("name")
    return "Hello, {}!!".format(name)




if __name__ == "__main__":
    app.run()


