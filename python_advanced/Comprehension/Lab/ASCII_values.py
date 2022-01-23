chars_list = input().split(', ')
result = {char: ord(char) for char in chars_list}
print(result)