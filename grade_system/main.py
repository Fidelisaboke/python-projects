# Main program - To call the functions from the grade.py module:

import grade
from time import sleep

students={}
marks_list=[]

while True:
    
    # Main menu
    print('''--STUDENT GRADE SYSTEM--
    Welcome to the student grade system!
    Select an option below:
    1 - View student list
    2 - Register student
    3 - Change student's name
    4 - Delete student
    5 - Enter marks
    6 - Find average/total marks for a student
    0 - Exit
    ''')

    # Checking the option that has been selected.
    option = input('> ')
    if option == '1':
        grade.display_students(students)
        sleep(2)
    elif option == '2':
        grade.reg_student(students)
        sleep(1.5)
    elif option == '3':
        grade.change_student_name(students)
        sleep(2)
    elif option == '4':
        grade.delete_student(students)
        sleep(2)
    elif option == '5':
        grade.enter_marks(students, marks_list)
        sleep(1.5)
    elif option == '6':
        grade.display_total_and_average(marks_list)
        sleep(2)
    elif option == '0':
        print('Closing...')
        sleep(2)
        break
    else:
        print('Please select a valid option and try again.')
        sleep(1)
    
