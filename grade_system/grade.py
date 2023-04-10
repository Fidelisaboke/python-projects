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
    try:
        student_no = int(input('Enter student number: '))
    except ValueError:
        print('Integers only. Try again.')
        return
    except:
        print("An unknown error has occured.")

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
    try:
        student_no = int(input('Enter student number: '))
    except ValueError:
        print('Integers only. Try again.')
        return
    except:
        print("An unknown error has occured.")
        return
    
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
    try:
        student_id=int(input("Enter the student's ID no: "))
    except ValueError:
        print("Please enter an integer")
        return
    except:
        print("An error has occured")
        return
    
    if student_id in students.keys():
        del students[student_id]
        print('Student deleted successfully')
    else:
        print('Student does not exist. Try again.')     

def display_students(students):
    print(f'Registered students: {students}')
    
def enter_marks(students, marks_list):
    global student_number
    try:
        student_number = int(input('Enter student number: '))
        if student_number in students.keys():
            no_of_subjects = int(input('How many subjects? '))
            for i in range(no_of_subjects):
                print(f'---Subject no {i+1}---')
                mark = int(input('Enter mark: '))
                if mark >= 0 and mark <= 100:
                    marks_list.append(mark)
                else:
                    print('Marks range from 0 to 100. Please try again.')
                    return
    except ValueError:
        print("Please enter an integer.")
        return
            
    else:
        print('Student does not exist')
        return

def get_total_marks(marks_list):
    return sum(marks_list)

def calculate_average_marks(marks_list):
    total_marks = get_total_marks(marks_list)
    
    try:
        average_marks  = total_marks/len(marks_list)
        return average_marks
    except ZeroDivisionError:
        print('No marks have been entered. Try again.')
        return
    
def get_student_number():
    return student_number

def display_average_marks(marks_list):
    average_marks = calculate_average_marks(marks_list)
    stud_no = get_student_number()
    print(f"Average marks for {stud_no}: {average_marks}")