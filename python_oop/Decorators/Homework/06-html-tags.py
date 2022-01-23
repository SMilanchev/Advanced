def tags(tag):
    def decorator(func):
        def wrapper(*args):
            res = func(*args)
            return f"<{tag}>{res}</{tag}>"

        return wrapper

    return decorator


@tags('b')
@tags('u')
@tags('i')
def to_upper(text):
    return text.upper()

print(to_upper('hello'))