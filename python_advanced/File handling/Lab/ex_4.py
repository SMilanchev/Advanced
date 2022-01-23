import os
#
#
# try:
#     os.remove('text_file.txt')
#     print('File deleted!')
# except FileNotFoundError:
#     print('File already deleted!')

if os.path.exists('my_first_file.txt'):
    os.remove('my_first_file.txt')
    print('File deleted!')
else:
    print('File already deleted!')