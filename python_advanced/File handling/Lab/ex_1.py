try:
    with open('text_file.txt') as file:
        print('File found')
except FileNotFoundError:
    print('File not found')