from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        member_id = 4
        session_date = "2024-12-15"
        duration_minutes = 10
        calories_burned = 100

        query = "INSERT INTO WorkoutSessions (member_id, session_date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"

        cursor.execute(query, (member_id, session_date, duration_minutes, calories_burned))
        conn.commit()
        print("Workout added successfully!")

    finally:
        cursor.close()
        conn.close()