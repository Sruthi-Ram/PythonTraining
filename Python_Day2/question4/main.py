from school import students, teachers, results

name = input("Enter student name: ")
roll = input("Enter roll number: ")
students.add_student(name, roll)

tname = input("Enter teacher name: ")
subject = input("Enter subject assigned: ")
teachers.assign_subject(tname, subject)

marks = float(input("Enter marks: "))
grade = results.calculate_grade(marks)

print("\n--- Report Card ---")
for s in students.view_students():
    print("Name:", s['name'])
    print("Roll No:", s['roll_no'])

for t, subj in teachers.view_teacher_info().items():
    print("Teacher:", t)
    print("Subject:", subj)

print("Marks:", marks)
print("Grade:", grade)
