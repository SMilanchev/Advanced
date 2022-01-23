text = input().split(', ')

text = [f'{word} -> {len(word)}' for word in text]
print(', '.join(text))