def print_result(list_result):
    for element in list_result:
        (char, value) = element
        print(f'{char}: {value} time/s')


text = input()

chars_occurrence_dict = {}
for ch in text:

    if ch not in chars_occurrence_dict:
        chars_occurrence_dict[ch] = 0
    chars_occurrence_dict[ch] += 1

print_result(sorted(chars_occurrence_dict.items()))
