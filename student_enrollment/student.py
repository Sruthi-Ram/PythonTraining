from config import get_connection
from mysql.connector import Error

class StudentDB:
    def add_student(self, name, email):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students (name, email) VALUES (%s, %s)",
                (name, email)
            )
            conn.commit()
            print(f"Student '{name}' added.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def list_students(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            for row in cursor.fetchall():
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
