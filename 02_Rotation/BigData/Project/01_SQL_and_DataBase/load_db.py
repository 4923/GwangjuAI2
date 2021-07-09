import sqlite3 as sql
from sqlite3.dbapi2 import connect

connection = sql.connect("customer.db")
cur = connection.cursor()
cur.execute(
    """CREATE TABLE customers(
    frist_name text, last_name text,
    email text)"""
)
connection.commit()
connection.close()

# commit은 언제 써야하나?
# https://docs.python.org/ko/3/library/sqlite3.html

from display import display

print(display)
