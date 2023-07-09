from time import sleep
import file_generator as file_gen

while True:
    print('''
          $File Generator$
          Please select an option:
          1. Generate text file
          2. Generate html file
          3. Exit
          ''')
    
    option = input('>')
    if option == '1':
        print('Text file Generator')
        file_count = int(input('Enter no of files: '))
        file_gen.create_text_file(file_count)
    elif option == '2':
        print('HTML file generator')
        file_count = int(input('Enter no of files: '))
        file_gen.create_html_file(file_count)
    elif option == '3':
        print('Exiting')
        sleep(2)
        break
    else:
        print('Please select a valid option')