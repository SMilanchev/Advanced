import os


def create_file(file_path):
    with open(file_path, 'w') as file:
        file.write("")


def add_file(file_path, content):
    with open(file_path, 'a') as file:
        file.writelines(content+'\n')


def replace_file(file_path, old_string, new_string):
    if not os.path.exists(file_path):
        print('An error occurred')
    else:
        with open(file_path) as file:
            text = file.readlines()
        with open(file_path, 'w') as file:
            for i in range(len(text)):
                text[i] = text[i].replace(old_string, new_string)
                file.write(text[i])


def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print('An error occurred')


END_COMMAND = 'End'
while True:
    input_command = input().split('-')
    command = input_command[0]
    if command == END_COMMAND:
        break
    file_path = input_command[1]
    if command == 'Create':
        create_file(file_path)
    elif command == 'Add':
        content = input_command[2]
        add_file(file_path, content)
    elif command == 'Replace':
        old_string, new_string = input_command[2:]
        replace_file(file_path, old_string, new_string)
    elif command == 'Delete':
        delete_file(file_path)
