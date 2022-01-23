dqdo = None
print(dqdo)

def outer():
    dqdo = None

    def get_dqdo():
        return dqdo

    def inner():
        #global dqdo
        print(dqdo)
        print('i1:', dqdo)
        dqdo = 42
        print('i2:', dqdo)

        return get_dqdo

    return inner



inner_func = outer()
func_get_dqdo = inner_func()
print(func_get_dqdo())
print(dqdo)