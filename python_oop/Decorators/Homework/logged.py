def logged(fn):
    def wrapper(*args, **kwargs):
        result = f'you called {fn.__name__}{(args)}\n'
        result += 'it returned {}'.format(fn(*args, **kwargs))
        return result
    return wrapper


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))