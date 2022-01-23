from Testing.Exercise.project.project.mammal import Mammal

import unittest


class MammalTest(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal('Zaiko', 'Rabbit', 'kweek')

    def test_mammal_is_initialized_properly(self):
        self.assertEqual(self.mammal.name, 'Zaiko')
        self.assertEqual(self.mammal.type, 'Rabbit')
        self.assertEqual(self.mammal.sound, 'kweek')

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), f'{self.mammal.name} makes {self.mammal.sound}')

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), 'animals')

    def test_info(self):
        result = self.mammal.info()
        expected = f"{self.mammal.name} is of type {self.mammal.type}"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()