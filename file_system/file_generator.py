''' 
FILE GENERATOR by Fidel Isaboke
-> This python script contains functions for creating duplicate files of various types
'''
from time import sleep

# .txt file generator
def create_text_file(files_count):
    for i in range(files_count):
        
        # Create a file
        html_file = open(f"file{i}.txt", "x")
        html_file.close()

        # Open the file in write mode
        html_file = open(f"file-{i}.txt", "w")
        
        # Write content to the file:
        html_file.write(f'FILE-{i+1}')
        html_file.close()
        
        # Delay execution for 1 second
        sleep(1)

# .html file generator
def create_html_file(files_count):
    for i in range(files_count):
        
        # Create a file
        html_file = open(f"page-{i}.html", "x")
        html_file.close()

        # Open the file in write mode
        html_file = open(f"page-{i}.txt", "w")
        
        # Write content to the file:
        html_file.write(f'''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Page {i}</title>
                </head>
                <body>
                    <h2>Page {i}</h2>
                    <hr>
                </body>
                </html>
                ''')
        
        html_file.close()
        
        # Delay execution for 1 second
        sleep(1)