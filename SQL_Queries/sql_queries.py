import sqlite3

dbfile = 'data.db'
connection = sqlite3.connect(dbfile)
cursor = connection.cursor()

query = """
SELECT * FROM albums
WHERE Title LIKE '%Live%' 
AND LENGTH(Title) > 10
"""
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(f'{row[0]}: {row[1]}')
cursor.close()
connection.close()
