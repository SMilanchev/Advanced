# try:
#     with open('text_file.txt', 'r') as file:
#         print('File found')
#         print(file.readline())
#         print(file.readlines(4))
#         print(file.read(10))
# except FileNotFoundError:
#     print('File not found')
#
# with open('text_file.txt') as file:
#     print(file.read())

# text = ['niki e pedal', 'hosi ne e pedal', 'ivacho e zena']
# print(''.join(text))
# ll = ['First line', 'Second line']

# with open('text.txt', 'w') as file:
#     for el in ll:
#         file.writelines(el)
# # for i in range(len(text)):
# #     text[i] = text[i].replace('First', '1st')
# #     print(text[i])
# #
# # print(text)
#

ll = ['index.html', 'index.js', 'demo.pptx', 'program.py', 'python.py', 'log.txt', 'notes.txt']
dd = {}
for el in ll:
    if el.split('.')[1] not in dd:
        dd[el.split('.')[1]] = []
    dd[el.split('.')[1]].append(el)

print(dd)

