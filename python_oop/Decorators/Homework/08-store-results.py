class store_results:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        func_result = self.fn(*args, **kwargs)
        result = "Function '{function}' was called. Result {result}'".format(function=self.fn.__name__, result=func_result)
        with open('results.txt', 'a') as file:
            file.write(result + '\n')


@store_results
def add(a, b):
    return a + b


@store_results
def mult(c, d):
    return c / d

with open('results.txt', 'w') as f:
    pass

add(3, 2)
mult(4, 2)