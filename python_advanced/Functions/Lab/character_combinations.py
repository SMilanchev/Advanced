def permutation(text, idx):
    if idx == len(text):
        print(''.join(text))
        return
    permutation(text, idx + 1)
    for i in range(idx + 1, len(text)):
        text[idx], text[i] = text[i], text[idx]
        permutation(text, idx + 1)
        text[i], text[idx] = text[idx], text[i]


text = list(input())
permutation(text, 0)
