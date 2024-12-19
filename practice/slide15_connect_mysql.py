import mysql.connector
from mysql.connector import Error

def connect_database():
    db_name = "e_commerce_db3"
    user = "root"
    password = "Lynn060386!"
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database=db_name,
            user = user,
            password = password,
            host = host
        )

        print("Connected to MySQL database successfully")
        return conn
    
    except Error as e:
        print(f"Error: {e}")
        return None