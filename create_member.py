from main import connect_database
import mysql.connector
from mysql.connector import Error

def add_member(name, age, trainer_id):
    
    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()
            
            new_member = [id, name, age]

            query = "INSERT INTO members (id, name, age) VALUES (%s, %s, %s)"

            cursor.execute(query, new_member)
            conn.commit()
            print("New member added succesfully")

        except Error as e:
            print(f"Error: {e}")

        finally:
            print("Closing cursor and connection...")
            cursor.close()
            conn.close()

add_member(5, "Vitorio Storraro", 72)