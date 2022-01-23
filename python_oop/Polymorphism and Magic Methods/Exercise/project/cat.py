from .animal import Animal


class Cat(Animal):
    def __repr__(self):
        return 'This is {name}. {name} is a {age} year old {gender} {class_name}'.format(
            name=self.name,
            age=self.age,
            gender=self.gender,
            class_name=self.__class__.__name__
        )

    def make_sound(self):
        return f"Meow meow!"

