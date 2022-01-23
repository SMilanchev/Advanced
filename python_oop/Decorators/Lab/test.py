# message = 'Lorem ipsum doler sit amet'
#
# def print_message(message):
#     def message_sender():
#         print('Closure')
#         print(message)
#     return message_sender()
#
#
# fn = print_message(message)
# def execute(fn):
#     return fn()
#
# def uppercase(fn):
#     def wrapper():
#         result = fn()
#         return result.upper()
#     return wrapper
#
# @uppercase # say_hi = uppercase(say_hi)
# def say_hi():
#     return 'Hi!'
#
# print(say_hi())
#
# def name_and_residence(fn):
#     def wrapper(*args):
#         result = fn(*args)
#         return result + ' and im from Sofia'
#     return wrapper
#
#
# @name_and_residence
# def say_my_name(name):
#     return f'I am {name}'
#
# print(say_my_name('Simco'))
# import time
#
# def measure_time(fn):
#     def wrapper(*args):
#         start = time.time()
#         result = fn(*args)
#         end = time.time()
#         return f'Total time: {end - start}'
#     return wrapper
#
#
# # @measure_time
# def say_hi():
#     time.sleep(1)
#     return
#
# res = measure_time(say_hi)()
# print(res)

def increase(n):
    def inner(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            return [i + n for i in result]

        return wrapper

    return inner


# @increase(2)
def get_numbers():
    return [1, 2, 3, 4, 5]




