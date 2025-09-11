from config import get_connection
from mysql.connector import Error

class CourseDB:
    def add_course(self, course_name, credits):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO courses (course_name, credits) VALUES (%s, %s)",
                (course_name, credits)
            )
            conn.commit()
            print(f"Course '{course_name}' added.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def list_courses(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM courses")
            for row in cursor.fetchall():
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
