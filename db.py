import sqlite3
import csv
con = sqlite3.connect("sql/db.sqlite")
con.text_factory = str
cur = con.cursor()

# cur.execute("""create table IF NOT EXISTS rotten(
#                 title varchar(100),
#                 critic_fresh varchar(20),
#                 user_fresh varchar(20)
#                 )""")

# query_str = "insert into rotten values (:title, :critic_fresh, :user_fresh)"
# params = {
#     "title":"기생충",
#     "critic_fresh":"99%",
#     "user_fresh":"99%"
# }
# cur.execute(query_str,params)
# 로튼토마토
# rotten_csv_file = open("rottentomato/rottencrawl.csv","rt", encoding='UTF8')
# rotten_csv_reader = csv.reader(rotten_csv_file)
# rotten_movie_list = list(rotten_csv_reader)
# rotten_movie_list = rotten_movie_list[1:]
# for item in rotten_movie_list:
#     item[0] = item[0].strip()
#     item[1] = item[1].strip()
#     item[2] = item[2].strip()
#
# print(rotten_movie_list)
#
# # CSV 로 읽은 데이터 테이블에 INSERT
#
# cur.executemany("insert into rotten values(?,?,?)",rotten_movie_list)
#
# cur.execute("select * from rotten")
# print(cur.fetchall())



# 씨네21

# cur.execute("""create table if not exists cine21(
#                 poster varchar(255),
#                 title varchar(100),
#                 date varchar(100),
#                 audience varchar(255),
#                 genre varchar(100),
#                 story text,
#                 review text,
#                 director varchar(100),
#                 actor varchar(255),
#                 cine varchar(100),
#                 netizens varchar(100))""")

cine_csv_file = open("db/cine.csv","rt", encoding='utf8')
cine_csv_reader = csv.reader(cine_csv_file)
cine = list(cine_csv_reader)
cine = cine[1:]
for item in cine:
    item[1] = item[1].strip()
    item[2] = item[2].strip()
    item[3] = item[3].strip()
    item[4] = item[4].strip()

cur.executemany("insert into cine21 values(?,?,?,?,?,?,?,?,?,?,?)", cine)
# cur.execute("select * from rotten")
# print(cur.fetchall())
con.commit()
