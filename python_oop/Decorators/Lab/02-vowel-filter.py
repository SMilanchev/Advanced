VOWELS = "aeouyi"


def vowel_filter(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return [el for el in result if el in VOWELS]
    return wrapper



@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
