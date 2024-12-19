from slide15_connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        updated_customer = ("9876543210", 5)

        query = "UPDATE Customers SET phone = %s WHERE id = %s"

        cursor.execute(query, updated_customer)
        conn.commit()
        print("Customer details updated successfully")
    
    finally:
        cursor.close()
        conn.close()