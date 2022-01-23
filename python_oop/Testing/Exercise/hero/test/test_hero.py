from Testing.Exercise.hero.project.hero import Hero
import parameterized
import unittest


class HeroTest(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('Warrior', 6, 78, 31)

    def test_hero_is_properly_initialized(self):
        self.assertEqual(self.hero.username, 'Warrior')
        self.assertEqual(self.hero.level, 6)
        self.assertEqual(self.hero.health, 78)
        self.assertEqual(self.hero.damage, 31)

    def test_battle_raises_exception_when_same_username(self):
        enemy = Hero('Warrior', 1, 1, 1)
        self.assertRaises(Exception, self.hero.battle, enemy)

    def test_battle_raises_exception_when_health_zero_or_negative(self):
        enemy = Hero('Warrior2', 2, 2, 2)
        for i in range(-3, 1):
            self.hero.health = i
            self.assertRaises(ValueError, self.hero.battle, enemy)

    def test_battle_raises_exception_when_enemy_health_zero_or_negative(self):
        for i in range(-3, 1):
            enemy = Hero('Warrior2', 2, i, 2)
            with self.assertRaises(Exception) as exc:
                self.hero.battle(enemy)
            self.assertEqual(str(exc.exception), f'You cannot fight {enemy.username}. He needs to rest')
            # self.assertRaises(ValueError, self.hero.battle, enemy)

    def test_battle_draw(self):
        enemy = Hero('Warrior2', 1, 12, 80)
        self.assertEqual(self.hero.battle(enemy), 'Draw')

    def test_battle_you_win(self):
        enemy = Hero('Warrior2', 1, 12, 5)
        self.assertEqual(self.hero.battle(enemy), 'You win')
        self.assertEqual(self.hero.level, 7)
        self.assertEqual(self.hero.health, 78)
        self.assertEqual(self.hero.damage, 36)

    def test_battle_you_lose(self):
        enemy = Hero('Warrior2', 3, 200, 30)
        self.assertEqual(self.hero.battle(enemy), 'You lose')
        self.assertEqual(enemy.username, 'Warrior2')
        self.assertEqual(enemy.level, 3 + 1)
        self.assertEqual(enemy.health, 200 - (self.hero.level * self.hero.damage) + 5)
        self.assertEqual(enemy.damage, 30 + 5)

    def test_hero_str(self):
        result = self.hero.__str__()
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                   f"Health: {self.hero.health}\n" \
                   f"Damage: {self.hero.damage}\n"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
