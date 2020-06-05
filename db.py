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

csv_file = open("rottentomato/rottencrawl.csv","rt", encoding='UTF8')
csv_reader = csv.reader(csv_file)
movie_list = list(csv_reader)
movie_list = movie_list[1:]
for item in movie_list:
    item[0] = item[0].strip()
    item[1] = item[1].strip()
    item[2] = item[2].strip()

print(movie_list)

# CSV 로 읽은 데이터 테이블에 INSERT

cur.executemany("insert ignore into rotten values(?,?,?)",movie_list)

cur.execute("select * from rotten")
print(cur.fetchall())
con.commit()