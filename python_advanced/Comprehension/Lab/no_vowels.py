VOWELS = {'a', 'o', 'u', 'e', 'i'}
VOWELS = VOWELS.union({x.upper() for x in VOWELS})
string = input()
new_string = [ch for ch in string if ch not in VOWELS]
print(''.join(new_string))
