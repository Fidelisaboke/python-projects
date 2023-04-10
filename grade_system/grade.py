# Module for the program functions

'''
Functions to implement:
- Adding a student - name and number
- Modifying a student's name
- Deleting a student
- Adding a student's marks 
- Getting their average
'''

import re
name_regex = r'^[A-Z][a-z]*$'

def check_input(input_string):
    return bool(re.match(name_regex, input_string))
    
def reg_student(students):
    try:
        student_no = int(input('Enter student number: '))
        student_name = input('Enter student name: ')
        if check_input(student_name):
            students.update({student_no:student_name})
        else:
            print('Error. Have you enetered the name correctly?')
    except:
        print('An error has occured. Please try again.')
        
def display_students(students):
    print(f'Registered students: {students}')
    
def enter_marks(students):
    student_number = int(input('Enter student number: '))
    if student_number in students.keys():
        no_of_subjects = int(input('How many subjects? '))