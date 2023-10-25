import unittest
from proj import divide_list

class TestDivideList(unittest.TestCase):
    def test_divide_list(self):
        self.assertEqual(divide_list([1, 2, 3, 4, 5, 6]), 0.6666666666666666)

if __name__ == '__main__':
    unittest.main()