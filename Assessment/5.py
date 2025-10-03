import pymysql

con = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    port=3306,
    database="riper"
)

cursor = con.cursor()

# cursor.execute("create database riper")
cursor.execute("""
CREATE TABLE customer (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20),
    model VARCHAR(20),
    phone VARCHAR(20),
    issue VARCHAR(50)
)
""")

