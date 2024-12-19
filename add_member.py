from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # query = "SELECT * FROM Customers"
        # cursor.execute(query)
        # for row in cursor.fetchall():
        #     print(row)

        new_member = (4, "John Doe", 40)

        query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"

        cursor.execute(query, new_member)
        conn.commit()
        print("New member added successfully")
    
    finally:
        cursor.close()
        conn.close()