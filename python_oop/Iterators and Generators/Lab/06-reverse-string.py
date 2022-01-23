reverse_text = lambda s: (char for char in reversed(s))

print(list(reverse_text('step')))
for c in reverse_text('step'):
    print(c, end='')