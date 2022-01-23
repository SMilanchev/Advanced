import re


def get_file_content(path_to_file):
    with open(path_to_file, 'r') as file:
        text = ''.join(file.readlines())
        return re.findall(r"[A-Za-z']+", text.lower())


def write_result_in_file(path_to_file, result):
    with open(path_to_file, 'w') as file:
        file.writelines('\n'.join(result))


path_to_words = 'words.txt'
path_to_text = 'text.txt'
text_file = get_file_content(path_to_text)
word_file = get_file_content(path_to_words)


analyze = {}
for word in word_file:
    if word in text_file:
        analyze[word] = text_file.count(word)

analyze = sorted(analyze.items(), key=lambda x: -x[1])
result = [f'{item[0]} - {item[1]}'for item in analyze]

result_path = 'output.txt'
write_result_in_file(result_path, result)