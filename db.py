import sqlite3
import csv
con = sqlite3.connect("sql/MoviewerDB.sqlite")
con.text_factory = str
cur = con.cursor()

# cur.execute("""create table IF NOT EXISTS rotten(
#                 ID INTEGER PRIMARY KEY autoincrement,
#                 poster varchar,
#                 title varchar,
#                 critic_fresh varchar,
#                 user_fresh varchar
#                 )""")
# # cur.execute("""create table IF NOT EXISTS rotten(
# #                 ID INTEGER PRIMARY KEY,
# #                 title varchar(100)
# #                 )""")
# con.commit()

# cur.execute("insert into rotten(poster,title,critic_fresh,user_fresh)"
#             "values('포스터','제목','99%','99%')")
# con.commit()
# cur.execute("select * from rotten")
# query_str = "insert into rotten values (:title, :critic_fresh, :user_fresh)"
# params = {
#     "title":"기생충",
#     "critic_fresh":"99%",
#     "user_fresh":"99%"
# }
# cur.execute(query_str,params)
# 로튼토마토
# rotten_csv_file = open("rottentomato/testr.csv","rt", encoding='UTF8')
# rotten_csv_reader = csv.reader(rotten_csv_file)
# rotten_movie_list = list(rotten_csv_reader)
# rotten_movie_list = rotten_movie_list[1:]
# for item in rotten_movie_list:
#     item[0] = item[0].strip()
#     item[1] = item[1].strip()
#     item[2] = item[2].strip()
#     item[3] = item[3].strip()
#
# print(rotten_movie_list)
#
# #CSV 로 읽은 데이터 테이블에 INSERT
#
# cur.executemany("insert into rotten(poster,title,critic_fresh,user_fresh) values(?,?,?,?)",rotten_movie_list)
# con.commit()




# 씨네21
#
# cur.execute("""create table if not exists cine21(
#                 ID INTEGER PRIMARY KEY autoincrement,
#                 poster varchar,
#                 title varchar,
#                 date varchar,
#                 audience varchar,
#                 genre varchar,
#                 story text,
#                 review text,
#                 director varchar,
#                 actor varchar,
#                 cine varchar,
#                 netizens varchar)""")
# con.commit()

cine_csv_file = open("cine.csv","rt", encoding='utf8')
cine_csv_reader = csv.reader(cine_csv_file)
cine = list(cine_csv_reader)
cine = cine[1:]
for item in cine:
    item[0] = item[0].strip()
    item[1] = item[1].strip()
    item[2] = item[2].strip()
    item[3] = item[3].strip()
    item[4] = item[4].strip()
    item[5] = item[5].strip()
    item[6] = item[6].strip()
    item[7] = item[7].strip()

cur.executemany("insert into cine21 (poster,title,date,audience,genre,story,review,director,actor,cine,netizens) values(?,?,?,?,?,?,?,?,?,?,?)", cine)
# cur.execute("select * from rotten")
# print(cur.fetchall())
con.commit()
