import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.compareTriplets([5, 6, 7], [3, 6, 10]), [1, 1])

    def test_case_1(self):
        self.assertEqual(my_code.compareTriplets([17, 28, 30], [99, 16, 8]), [2, 1])


if __name__ == '__main__':
    unittest.main()
