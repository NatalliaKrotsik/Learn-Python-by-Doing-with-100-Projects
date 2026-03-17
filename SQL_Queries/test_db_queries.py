from db_queries import get_german_invoices

def test_get_german_invoices():
    dbfile = "data.db"

    rows = get_german_invoices(dbfile)

    assert rows is not None
    assert len(rows) > 0

    for row in rows:
        billing_country = row[6]   # depends on table structure
        total = row[8]

        assert billing_country == "Germany"
        assert total >= 2.0