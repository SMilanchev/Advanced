

import unittest

from project.animal import Animal
from project.cat import Cat
from project.dog import Dog
from project.kitten import Kitten
from project.tomcat import Tomcat

animal = Animal('ime', 12, 'momchence')
print(animal.name)
print(animal.age)
print(animal.gender)