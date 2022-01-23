def read_file_content(file_path):
    with open(file_path) as file:
        return list((el.strip() for el in file.readlines()))


def find_punctuation_count(line, punctuation_symbols):
    counter = 0
    for el in punctuation_symbols:
        counter += line.count(el)
    return counter


def find_letters_count(text):
    counter = 0
    for ch in text:
        if ch.isalpha():
            counter += 1
    return counter


punctuation_symbols = ['-', ',', '.', '!', '?', "'"]
file_path_read_file = '../Lab/text.txt'
text_read_file = read_file_content(file_path_read_file)

result = []
for line in text_read_file:
    punctuation_counter = find_punctuation_count(line, punctuation_symbols)
    letter_counter = find_letters_count(line)
    result.append(f'{line} ({letter_counter})({punctuation_counter})')

path_target_file = 'output1.txt'
with open(path_target_file, 'w') as file:
    file.write('\n'.join(result))