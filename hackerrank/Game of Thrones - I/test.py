import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.gameOfThrones('aaabbbb'), 'YES')

    def test_case_1(self):
        self.assertEqual(my_code.gameOfThrones('cdefghmnopqrstuvw'), 'NO')

    def test_case_2(self):
        self.assertEqual(my_code.gameOfThrones('cdcdcdcdeeeef'), 'YES')


if __name__ == '__main__':
    unittest.main()
