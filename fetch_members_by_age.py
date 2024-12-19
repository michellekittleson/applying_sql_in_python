from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        query = "select * from Members WHERE age between 5 and 15"

        cursor.execute(query)

        for row in cursor.fetchall():
            print(row)

    finally:
        cursor.close()
        conn.close()