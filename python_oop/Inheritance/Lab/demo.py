# class Person:
#     def __init__(self, first_name, last_name, birth_year, gender, residence):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.residence = residence
#         self.birth_year = birth_year
#         self.gender = gender
#
#     def say_my_name(self):
#         return f'My name is: {self.first_name} {self.last_name}'
#
#
# class Student(Person):
#     def __init__(self, *args, **kwargs):
#         fac_num = kwargs.pop('faculty_number')
#         super().__init__(*args, **kwargs)
#         self.fac_num = fac_num
#
#     def __str__(self):
#         res = super().__str__()
#         return res + f'with fac num: {self.fac_num}'
#
#
# student = Student('ivan', 'ivanov', 1997, 'M', 'Bulgaria', faculty_number=191591)
# print(student.say_my_name())
# print(student.fac_num)
# print(Student.__mro__)

# class Person:
#     def __init__(self, name, father=None, mother=None):
#         self.name = name
#         self.father = father
#         self.mother = mother
#
#     def say_mothers_name(self):
#         return self.mother.name
#
#     def say_fathers_name(self):
#         return self.father.name
#
#
# mama = Person('mama')
# tate = Person('tate')
#
# son = Person('son', mother=mama, father=tate)
# print(son.say_fathers_name())
# print(son.say_mothers_name())

# class SimCardReader:
#     def send_signal(self):
#         return 'sending signal...'
#
#     def receive_signal(self):
#         return 'receiving signal...'
#
# class Display:
#     def show_on_display(self, value):
#         return value
#
# class Smartphone():
#     def __init__(self):
#         self.display = Display()
#         self.sim_card_reader = SimCardReader()
#
# class Tablet():
#     def __init__(self):
#         self.display = Display()
#
# phone = Smartphone()
# print(phone.display.show_on_display('displaying'))