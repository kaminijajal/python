import sqlite3

db = sqlite3.connect("mysql.db")

# db.execute("create table std(id int primery key auto_incement , name varchar(20),email varchar(30))")
db.execute("insert into  std values(2, 'kamini','kamini@gmail.com')")