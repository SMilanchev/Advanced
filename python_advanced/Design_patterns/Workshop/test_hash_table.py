from Hash_table import HashTable
import unittest
from unittest.mock import patch


class HashTableTest(unittest.TestCase):
    def test_is_HashTable_properly_initialized(self):
        self.assertEqual(HashTable().array, [None, None, None, None, None])

    def test_set(self):
        table = HashTable()
        table.set('Jim', 'value')
        table.set('Tim', 'value1')
        self.assertEqual('value', table.get('Jim'))
        self.assertEqual('value1', table.get('Tim'))

    def test_get(self):
        table = HashTable()
        table.set('12', 'ok')
        self.assertEqual(table.get('12'), 'ok')

    def test_last_key_value_paired_is_stored(self):
        table = HashTable()
        table.set('12', 'value')
        table.set('12', 'value1')
        self.assertEqual(table.get('12'), 'value1')

    def test_default_when_key_is_missing(self):
        self.assertEqual(HashTable().get('non existing'), None)
        self.assertEqual(HashTable().get('non existing', 'def par'), 'def par')

    def test_default_given_collision(self):
        with patch('Hash_table.hash') as mock:
            table = HashTable(capacity=1)
            mock.return_value = 1

        table.set('Jim', 'value')
        self.assertEqual('default', table.get('Tim', 'default'))

    def test_insert_more_elements_than_initial_capacity(self):
        table = HashTable(capacity=2)
        for n in range(3):
            table.set(n, n)
            self.assertEqual(n, table.get(n))

        self.assertLess(2, table.capacity)


if __name__ == '__main__':
    unittest.main()