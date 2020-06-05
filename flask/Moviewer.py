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

@app.route("/rotten/title")

def get_movie_by_title():
    title = request.args.get("title")

    with get_db_con() as con:
        cur=con.cursor()

        q = "select * from rotten where title like :title"
        param = {
            "title": "%" + title + "%"
        }

        result = cur.execute(q,param)

    result_json = jsonize(result)

    return result_json

@app.route("/hello")
def hello_to_get_param():
    name = request.args.get("name")
    return "Hello, {}!!".format(name)

def jsonize(result):
    result_json = json.dumps(list(result.fetchall()), ensure_ascii=False).encode("utf-8")
    return result_json


if __name__ == "__main__":
    app.run()


