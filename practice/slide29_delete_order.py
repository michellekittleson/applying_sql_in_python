from slide15_connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        customer_id = 1

        order_id = 6

        query = "DELETE FROM Orders WHERE id = %s AND customer_id = %s"

        cursor.execute(query, (order_id, customer_id))
        conn.commit()
        print("Order deleted successfully!")
    
    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()