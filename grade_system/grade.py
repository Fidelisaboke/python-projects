# Module for the program functions

'''
Functions to implement:
- Adding a student - name and number
- Deleting a student
- Adding a student's marks 
- Getting their average
'''

import re
name_regex = r'^[A-Z][a-z]*$'

# Check the format of the input
def check_input(input_string):
    return bool(re.match(name_regex, input_string))
    
def reg_student(students):
    student_no = int(input('Enter student number: '))
    student_name = input('Enter student name: ')
    if check_input(student_name):
        if student_no in students.keys():
            print('Student already exists. Try again.')
        else:
            students.update({student_no:student_name})
            print('Student registered successfully!')
    else:
        print('''Error. Have you enetered the name and ID correctly?
        ID: only numbers, Name: only a single name''')

def change_student_name(students):
    student_no = int(input('Enter student number: '))
    if student_no in students.keys():
        new_student_name = input('Enter new name: ')
        if check_input(new_student_name):
            students.update({student_no:new_student_name})
            print('Name changed successfully')
        else:
            print("Make sure you entered the name in the right format.")
    else:
        print('Student does not exist.')



def delete_student(students):
    student_id=int(input("Enter the student's ID no: "))
    if student_id in students.keys():
        del students[student_id]
        print('Student deleted successfully')
    else:
        print('Student does not exist. Try again.')     

def display_students(students):
    print(f'Registered students: {students}')
    
def enter_marks(students, marks_list):
    student_number = int(input('Enter student number: '))
    if student_number in students.keys():
        no_of_subjects = int(input('How many subjects? '))
        for i in range(no_of_subjects):
            print(f'---Subject no {i+1}---')
            mark = int(input('Enter mark: '))
            marks_list.append(mark)
    else:
        print('Student does not exist')

def calculate_total_marks(marks_list):
    return sum(marks_list)

def calculate_average_marks(marks_list):
    global total_marks
    global average_marks
    total_marks = calculate_total_marks(marks_list)
    
    try:
        average_marks  = total_marks/len(marks_list)
        return average_marks
    except ZeroDivisionError:
        print('No marks have been entered. Try again.')
        return 0

def display_total_and_average():
    print(f'Total marks: {total_marks}')
    print(f'Average: {average_marks}')