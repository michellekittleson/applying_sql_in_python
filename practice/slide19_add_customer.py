from slide15_connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        query = "SELECT * FROM Customers"
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)

        # new_customer = ("John Doe", "john@example.com", "1234567890")

        # query = "INSERT INTO Customers (name, email, phone) VALUES (%s, %s, %s)"

        # cursor.execute(query, new_customer)
        # conn.commit()
        # print("New customer added successfully")
    
    finally:
        cursor.close()
        conn.close()