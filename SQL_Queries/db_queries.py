import sqlite3

def get_german_invoices(dbfile):
    connection = sqlite3.connect(dbfile)
    cursor = connection.cursor()

    query = """
    SELECT * FROM invoices
    WHERE BillingCountry = 'Germany'
    AND Total >= 2.0
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows