import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.stoneDivision(12, [2, 3, 4]), 4)


if __name__ == '__main__':
    unittest.main()
