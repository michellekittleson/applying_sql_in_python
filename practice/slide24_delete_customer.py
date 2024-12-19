from slide15_connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        customer_to_remove = (5, )

        query_check = "SELECT * FROM Orders WHERE customer_id = %s"
        cursor.exrcute(query_check, customer_to_remove)
        orders = cursor.fetchall()

        if orders:
            print("Cannot delete customer: Customer has associated orders.")
        else:

            query = "DELETE FROM Customers WHERE id = %s"

            cursor.execute(query, customer_to_remove)
            conn.commit()
            print("Customer removed successfully")
    
    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()