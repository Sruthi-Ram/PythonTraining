student_list = []

def add_student(name, roll_no):
    student_list.append({'name': name, 'roll_no': roll_no})

def view_students():
    return student_list
