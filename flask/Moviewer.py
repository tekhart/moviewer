from flask import Flask
from flask import request
import json
import sqlite3

app = Flask(__name__)

app.debug = True


def get_db_con() -> sqlite3.connect: return sqlite3.connect('../sql/db.sqlite')


# 로튼토마토
@app.route("/rotten")
def hello():
    with get_db_con() as con:
        cur = con.cursor()

        q = "select * from rotten"
        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json



@app.route("/rotten/title")
def get_movie_by_title():

    with get_db_con() as con:
        cur=con.cursor()

        q = "select * from rotten order by 1"

        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json

@app.route("/rotten/critic_score")
def hello_to_get_param():
    with get_db_con() as con:
        cur = con.cursor()

        q = "select * from rotten order by 2 DESC"

        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json

# @app.route("/rotten/user_score")
# def hello_to_get_param():
#     with get_db_con() as con:
#         cur = con.cursor()
#
#         q = "select * from rotten order by 3 DESC"
#
#         result = cur.execute(q)
#
#     result_json = jsonize(result)
#
#     return result_json
#
# #씨네21
# @app.route("/cine")
# def get_rotten_movie():
#     with get_db_con() as con:
#         cur = con.cursor()
#
#         q = "select * from cine21"
#         result = cur.execute(q)
#
#     result_json = jsonize(result)
#
#     return result_json
#
# @app.route("/cine21/title")
# def get_movie_by_title():
#
#     with get_db_con() as con:
#         cur=con.cursor()
#
#         q = "select * from rotten order by 2"
#
#         result = cur.execute(q)
#
#     result_json = jsonize(result)
#
#     return result_json

def jsonize(result):
    result_json = json.dumps(list(result.fetchall()), ensure_ascii=False).encode("utf-8")
    return result_json


if __name__ == "__main__":
    app.run()
