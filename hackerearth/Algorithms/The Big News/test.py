import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '7',
        '4',
        '3',
        '2 5 4',
        '2',
        '1 2',
        '1',
        '1',
        '2',
        '6 7',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue().strip(), '4 4 1 4 4 2 2')


if __name__ == '__main__':
    unittest.main()
