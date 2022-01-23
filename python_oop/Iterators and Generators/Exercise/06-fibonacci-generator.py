def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b



fibo = fibonacci()
for f in range(5):
    print(next(fibo))
