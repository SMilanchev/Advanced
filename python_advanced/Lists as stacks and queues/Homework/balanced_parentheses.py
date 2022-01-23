string = input()
is_break = False
parentheses_dict = {'{': '}', '[': ']', '(': ')'}
elements = []

for p in string:
    if p in parentheses_dict.keys():
        elements.append(p)
    else:
        if not elements:
            is_break = True
            break
        current_p = elements.pop()
        if not parentheses_dict[current_p] == p:
            is_break = True
            break

if is_break:
    print('NO')
else:
    print('YES')
