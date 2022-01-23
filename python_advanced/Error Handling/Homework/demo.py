import re
user = 'petergmail.com'
word = re.match(r'[a-zA-Z]+@', user)
word.span()
print(word.span())
# print(len(re.findall(r'[a-zA-Z]+@', user)[0]))
# it_len = len(str(re.findall(r'[a-zA-Z]+@', user)))
# print(it_len)
# # print(len(re.finditer(r'[a-zA-Z]+@', user)))