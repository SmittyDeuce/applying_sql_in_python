import mysql.connector
from mysql.connector import Error

def connect_database():

    db_name = 'gym_db'
    user = "root"
    password = "Ibewlu332$@$!!"
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )


        print("Connection to database succesful!")
        return conn

    except Error as e:
        print(f"Error: {e}")
        return None
    

def add_member(name, age, trainer_id):
    conn = connect_database()
    
    if conn is not None:
        try:
            cursor = conn.cursor()

            # Insert new member
            insert_query = """
            INSERT INTO members (name, age, trainer_id)
            VALUES (%s, %s, %s)
            """
            member_data = (name, age, trainer_id)
            cursor.execute(insert_query, member_data)
            conn.commit()

            print("New member added successfully.")

        except mysql.connector.Error as e:
            print(f"Error adding member: {e}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


# add_member('John Doe', 30, 1)


def add_workout_session(member_id, date, duration_minutes, calories_burned, trainer_id):
    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()

            # Check if member_id exists in members table
            cursor.execute("SELECT id FROM members WHERE id = %s", (member_id,))
            member_exists = cursor.fetchone()

            if not member_exists:
                print(f"Error: Member with ID {member_id} does not exist.")
                return

            # Insert new workout session
            insert_query = """
            INSERT INTO Workout_Sessions (member_id, date, duration_minutes, calories_burned, trainer_id)
            VALUES (%s, %s, %s, %s, %s)
            """
            session_data = (member_id, date, duration_minutes, calories_burned, trainer_id)  # Include trainer_id here
            cursor.execute(insert_query, session_data)
            conn.commit()

            print("Workout session added successfully.")

        except mysql.connector.Error as e:
            print(f"Error adding workout session: {e}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


# add_workout_session(2, '2024-06-28', 60, 300, 1)


def update_member_age(member_id, new_age):
    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()

            # Check if member_id exists in members table
            cursor.execute("SELECT id FROM members WHERE id = %s", (member_id,))
            member_exists = cursor.fetchone()

            if not member_exists:
                print(f"Error: Member with ID {member_id} does not exist.")
                return

            # Update member age
            update_query = """
            UPDATE members
            SET age = %s
            WHERE id = %s
            """
            cursor.execute(update_query, (new_age, member_id))
            conn.commit()

            print("Member age updated successfully.")

        except mysql.connector.Error as e:
            print(f"Error updating member age: {e}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


# update_member_age(2, 55)

def delete_workout_session(session_id):
    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()

            # Check if session_id exists in Workout_Sessions table
            cursor.execute("SELECT id FROM Workout_Sessions WHERE id = %s", (session_id,))
            session_exists = cursor.fetchone()

            if not session_exists:
                print(f"Error: Workout session with ID {session_id} does not exist.")
                return

            # Delete workout session
            delete_query = "DELETE FROM Workout_Sessions WHERE id = %s"
            cursor.execute(delete_query, (session_id,))
            conn.commit()

            print(f"Workout session with ID {session_id} deleted successfully.")

        except mysql.connector.Error as e:
            print(f"Error deleting workout session: {e}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


# delete_workout_session(1)

def get_members_in_age_range(start_age, end_age):
    conn = connect_database()
    
    if conn is not None:
        try:
            cursor = conn.cursor()

            # SQL query to retrieve members within the age range
            select_query = """
            SELECT id, name, age, trainer_id 
            FROM members 
            WHERE age BETWEEN %s AND %s
            """
            cursor.execute(select_query, (start_age, end_age))
            results = cursor.fetchall()

            for row in results:
                print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Trainer ID: {row[3]}")

        except mysql.connector.Error as e:
            print(f"Error retrieving members: {e}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


get_members_in_age_range(25, 30)