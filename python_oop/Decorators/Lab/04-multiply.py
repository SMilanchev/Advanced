def multiply(times):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs) * times

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))