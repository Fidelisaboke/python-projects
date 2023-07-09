''' 
FILE GENERATOR by Fidel Isaboke
-> This python script contains functions for creating duplicate files of various types
'''
from time import sleep

# .txt file generator
def create_text_file(files_count):
    for i in range(files_count):
        
        # Create a file
        text_file = open(f"gen_files/text/file-{i}.txt", "x")
        text_file.close()

        # Open the file in write mode
        text_file = open(f"gen_files/text/file-{i}.txt", "w")
        
        # Write content to the file:
        text_file.write(f'This text file was automatically created.')
        text_file.close()
        
        print(f'text file {i} created.')
        
        # Delay execution for 0.5 seconds
        sleep(0.5)

# .html file generator
def create_html_file(files_count):
    for i in range(files_count):
        
        # Create a file
        html_file = open(f"gen_files/html/page-{i}.html", "x")
        html_file.close()

        # Open the file in write mode
        html_file = open(f"gen_files/html/page-{i}.html", "w")
        
        # Write content to the file:
        html_file.write(f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page {i}</title>
</head>
<body>
    <h2 style='text-align:center;'>Page {i}</h2>
    <hr>
</body>
</html>
''')
        
        html_file.close()
        
        print(f'html page {i} created')
        
        # Delay execution for 0.5 seconds
        sleep(0.5)
