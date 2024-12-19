from slide15_connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        query = """
        SELECT o.id AS OrderID, o.date AS OrderDate, c.id as CustomerID, c.name, c.email
        FROM Customers c, Orders o
        WHERE c.id = o.customer_id AND c.name LIKE 'Carol%';
        """

        cursor.execute(query)

        for order in cursor.fetchall():
            print(order)
    
    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()