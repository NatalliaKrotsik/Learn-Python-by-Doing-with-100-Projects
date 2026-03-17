import sqlite3

dbfile = 'data.db'
connection = sqlite3.connect(dbfile)
cursor = connection.cursor()

query = """
SELECT * FROM invoices
WHERE BillingCountry = 'Germany'
AND Total >= 2.0
"""
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
connection.close()