from student import StudentDB
from course import CourseDB
from enrollment import EnrollmentDB

student_db = StudentDB()
course_db = CourseDB()
enroll_db = EnrollmentDB()

# Add students
student_db.add_student("John", "john@example.com")
student_db.add_student("Alice", "alice@example.com")

# Add courses
course_db.add_course("Python Programming", 3)
course_db.add_course("Data Structures", 4)

# Enroll students
enroll_db.enroll_student(1, 1)  # John → Python
enroll_db.enroll_student(1, 2)  # John → Data Structures

# List John's courses
enroll_db.list_student_courses(1)

# Generate course-wise report
enroll_db.course_report()
