def type_check(input_type):
    def decorator(func):
        def wrapper(num):
            if not isinstance(num, input_type):
                return 'Bad Type'
            return func(num)

        return wrapper

    return decorator



@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello world'))
print(first_letter(["not a string"]))
