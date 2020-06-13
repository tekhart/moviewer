from flask import Flask
from flask import request
import json
import sqlite3

app = Flask(__name__, static_url_path='', static_folder="html")

app.debug = True


def get_db_con() -> sqlite3.connect: return sqlite3.connect('../sql/MoviewerDB.sqlite')


# 로튼토마토
@app.route("/rotten")
def get_rotten_movie():
    with get_db_con() as con:
        cur = con.cursor()

        q = "select * from rotten"
        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json

@app.route("/rotten/<title>")
def get_rotten_movie_detail(title):
    with get_db_con() as con:
        cur = con.cursor()

        q = "select * from rotten where title = '" + str(title) + "'"
        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json



@app.route("/rotten/title")
def get_rotten_movie_by_title():

    with get_db_con() as con:
        cur=con.cursor()

        q = "select * from rotten order by 3"

        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json

@app.route("/rotten/critic_score")
def get_rotten_movie_by_cscore():
    with get_db_con() as con:
        cur = con.cursor()

        q = "select * from rotten order by 4 DESC"

        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json

@app.route("/rotten/user_score")
def get_rotten_movie_by_uscore():
    with get_db_con() as con:
        cur = con.cursor()

        q = "select * from rotten order by 5 DESC"

        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json

#씨네21
@app.route("/cine21")
def get_cine_movie():
    with get_db_con() as con:
        cur = con.cursor()

        q = "select * from cine21"
        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json

@app.route("/cine21/title")
def get_cine_movie_by_title():

    with get_db_con() as con:
        cur=con.cursor()

        q = "select * from cine21 order by 3"

        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json


@app.route("/cine21/critic_score")
def get_cine_movie_by_cscore():

    with get_db_con() as con:
        cur=con.cursor()

        q = "select * from cine21 order by 10 DESC"

        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json

@app.route("/cine21/user_score")
def get_cine_movie_by_uscore():
    with get_db_con() as con:
        cur = con.cursor()

        q = "select * from cine21 order by 11 DESC"

        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json

def jsonize(result):
    result_json = json.dumps(list(result.fetchall()), ensure_ascii=False).encode("utf-8")
    return result_json


if __name__ == "__main__":
    app.run()
