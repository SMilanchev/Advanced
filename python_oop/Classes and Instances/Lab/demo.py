# a = 42
#
#
# class Baba:
#     a = 1
#     b = a + 1
#
#
#     def say_hi(self):
#         print(a)
#
#
# baba = Baba()
# baba.say_hi()
# class Dog:
#     kind = 'canine'
#
#     def __init__(self, name):
#         self.name = name

class Baba:
    number_of_instances = 0

    def __init__(self):
        Baba.number_of_instances += 1


baba_1 = Baba()
baba_2 = Baba()
baba_3 = Baba()
baba_4 = Baba()

print(Baba.number_of_instances)