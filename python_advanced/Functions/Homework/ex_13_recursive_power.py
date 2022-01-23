def recursive_power(num, degree):
    if degree == 1:
        return num
    return num * recursive_power(num, degree-1)


print(recursive_power(2, 10))
print(recursive_power(10, 100))
