def is_length_even(word):
    return len(word) % 2 == 0


text = input().split(' ')

[print(x) for x in text if is_length_even(x)]