from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        updated_member = (34, 4)

        query = "UPDATE Members SET age = %s WHERE id = %s"

        cursor.execute(query, updated_member)
        conn.commit()
        print("Member information updated successfully")
    
    finally:
        cursor.close()
        conn.close()