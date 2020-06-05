import sqlite3
import csv
con=sqlite3.connect("cinedb2.sqlite")
con.text_factory=str
cur=con.cursor()

cur.execute("""create table if not exists cine21(
                poster varchar(255),
                title varchar(100),
                date varchar(100),
                audience varchar(255),
                genre varchar(100),
                story text,
                review text,
                director varchar(100),
                actor varchar(255),
                cine varchar(100),
                netizens varchar(100))""")

cur.execute("insert into cine21 values(?,?,?,?,?,?,?,?,?,?,?)",
            ("포스터", "제목", "개봉일", "관람객", "장르", "줄거리", "리뷰", "감독", "배우", "씨네평점", "네티즌평점"))

csv_file = open("cine.csv", encoding='utf8')
csv_reader = csv.reader(csv_file)
cine = list(csv_reader)
cine = cine[1:]
for item in cine:
    item[1] = item[1].strip()
    item[2] = item[2].strip()
    item[3] = item[3].strip()
    item[4] = item[4].strip()
    cur.executemany("insert into cine21 values(?,?,?,?,?,?,?,?,?,?,?)", cine)

    con.commit()