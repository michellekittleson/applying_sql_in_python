from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        member_id = 1

        session_id = 1

        query = "DELETE FROM WorkoutSessions WHERE member_id = %s AND session_id = %s"

        cursor.execute(query, (member_id, session_id))
        conn.commit()
        print("Workout session deleted successfully!")
    
    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()