#This project, I will be working with the data from the CIA World
#Factbook, which is a compendium of statistics about all of the
#countries on Earth. This Factbook contains demographic information
#and can serve as an excellent way to practice SQL queries in
#conjunction with the capabilities of Python.
import pandas as pd
import sqlite3

#Making a connection to database.
conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()

#Lets run a query that returns the first 5 rows of the facts
#table in the databaseto see how how the table looks like.
q1 = "SELECT * FROM sqlite_master WHERE type='table';"
pd.read_sql_query(q1, conn)
cursor.execute(q1).fetchall()