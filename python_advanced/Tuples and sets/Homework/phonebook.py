def is_digit(entry):
    return entry.isdigit()


def print_result(phonebook, name):
    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')


operations_count = 0

phonebook = {}
while True:
    entry = input()
    if is_digit(entry):
        operations_count = int(entry)
        break
    (name, number) = entry.split('-')
    if name not in phonebook:
        phonebook[name] = ""
    phonebook[name] = number

for _ in range(operations_count):
    print_result(phonebook, input())