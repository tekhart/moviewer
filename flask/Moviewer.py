from flask import Flask
from flask import request
import json
import sqlite3

app = Flask(__name__, static_url_path='', static_folder="html")

app.debug = True


def get_db_con() -> sqlite3.connect: return sqlite3.connect('../sql/MoviewerDB.sqlite')


# 로튼토마토
@app.route("/rotten/list/<id>")
def get_rotten_movie(id):
    id = int(id)
    if id == 1:
        id = 1
    else:
        id = (id - 1) * 20
    with get_db_con() as con:
        cur = con.cursor()

        q = "select * from rotten where id >= " + str(id) + " order by id asc limit 20"
        print(q)
        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json
@app.route("/rotten/<id>")
def get_rotten_movie_detail(id):
    with get_db_con() as con:
        cur = con.cursor()

        q = "select * from rotten where id = '" + str(id) + "'"
        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json

@app.route("/rotten/search/<title>")
def get_rotten_movie_title(title):
    with get_db_con() as con:
        cur = con.cursor()

        q = "select * from rotten where title like '%" + str(title) + "%'"
        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json





#씨네21
@app.route("/cine21/list/<id>")
def get_cine_movie(id):
    id = int(id)
    if id == 1:
        id = 1
    else:
        id = (id - 1) * 20
    with get_db_con() as con:
        cur = con.cursor()

        q = "select * from cine21 where id >= " + str(id) + " order by id asc limit 20"
        print(q)
        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json


@app.route("/cine21/<id>")
def get_cine_movie_detail(id):
    with get_db_con() as con:
        cur = con.cursor()

        q = "select * from cine21 where id = '" + str(id) + "'"
        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json

@app.route("/cine21/search_movie/<title>")
def get_cine_movie_title(title):
    with get_db_con() as con:
        cur = con.cursor()

        q = "select * from cine21 where title like '%" + str(title) + "%'"
        result = cur.execute(q)

    result_json = jsonize(result)

    return result_json


def jsonize(result):
    result_json = json.dumps(list(result.fetchall()), ensure_ascii=False).encode("utf-8")
    return result_json


if __name__ == "__main__":
    app.run()
