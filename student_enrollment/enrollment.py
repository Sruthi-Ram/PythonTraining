from config import get_connection
from mysql.connector import Error
from datetime import date

class EnrollmentDB:
    def enroll_student(self, student_id, course_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (%s, %s, %s)",
                (student_id, course_id, date.today())
            )
            conn.commit()
            print(f"Student {student_id} enrolled in course {course_id}.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def list_student_courses(self, student_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT c.course_name, c.credits, e.enrollment_date
                FROM enrollments e
                JOIN courses c ON e.course_id = c.course_id
                WHERE e.student_id = %s
            """, (student_id,))
            for row in cursor.fetchall():
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def course_report(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT c.course_name, s.name, s.email, e.enrollment_date
                FROM enrollments e
                JOIN students s ON e.student_id = s.student_id
                JOIN courses c ON e.course_id = c.course_id
                ORDER BY c.course_name, s.name
            """)
            for row in cursor.fetchall():
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
