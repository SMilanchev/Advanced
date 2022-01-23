def get_file_content(file_path):
    with open(file_path) as file:
        return file.readlines()


def get_even_lines(text):
    return [element.strip() for element in text if text.index(element) % 2 == 0]


def reverse_and_replace(list_str, symbols, new_symbol):
    new_list = []
    for string in list_str:
        for symbol in symbols:
            string = string.replace(symbol, new_symbol)
        new_list.append(list(reversed(string.split(' '))))

    return new_list


def print_result(result):
    [print(' '.join(el)) for el in result]


file_path = '../Lab/text.txt'
text = get_file_content(file_path)
even_lines_text = get_even_lines(text)
symbols_to_be_replaced = ['-', ',', '.', '!', '?']
new_symbol = '@'
result = reverse_and_replace(even_lines_text, symbols_to_be_replaced, new_symbol)
print_result(result)