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
        try:
            file_count = int(input('Enter no of files: '))
            
            if file_count in range(1, 21, 1):
                file_gen.create_text_file(file_count)
            else:
                print("You can only create from 1 up to 20 files, otherwise the computer would be full :)")
        except:
            print('Integers only!')
            sleep(1)
    elif option == '2':
        print('HTML file generator')
        try:
            file_count = int(input('Enter no of files: '))
            if file_count in range(1, 21, 1):
                file_gen.create_html_file(file_count)
            else:
                print("You can only create from 1 up to 20 files, otherwise the computer would be full :)")
        except:
            print("Integers only!")
    elif option == '3':
        print('Exiting')
        sleep(1)
        break
    else:
        print('Please select a valid option')
        sleep(1)