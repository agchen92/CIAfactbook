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

#Now that we know that the facts table looks like. Lets run a few
#queries to gain some data insights.
q2 = '''SELECT * FROM facts LIMIT 5'''
pd.read_sql_query(q2, conn)

q3 = '''
SELECT min(population) min_pop, max(population) max_pop, 
min(population_growth) min_pop_grwth, max(population_growth) max_pop_grwth 
FROM facts
'''
pd.read_sql_query(q3, conn)

q4 = '''
SELECT *
FROM facts
WHERE population == (SELECT max(population) FROM facts);
'''

pd.read_sql_query(q4, conn)

q5 = '''
SELECT *
FROM facts
WHERE population == (SELECT min(population) FROM facts);
'''

pd.read_sql_query(q5, conn)

#Now that we have gained some insight regarding the data
#let's try to create some visualization to better present our findings

import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

q6 = '''
SELECT population, population_growth, birth_rate, death_rate
FROM facts
WHERE population != (SELECT max(population) FROM facts)
and population != (SELECT min(population) FROM facts);
'''
pd.read_sql_query(q6, conn).hist(ax=ax)

#Let's try to find which countries have the highest population.
q7 = '''SELECT name, CAST(population as float)/CAST(area as float) density 
FROM facts 
ORDER BY density DESC 
LIMIT 20'''
pd.read_sql_query(q7, conn)

q7 = '''SELECT population, population_growth, birth_rate, death_rate
FROM facts
WHERE population != (SELECT max(population) FROM facts)
and population != (SELECT min(population) FROm facts);
'''
pd.read_sql_query(q7, conn)