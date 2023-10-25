import unittest
from proj import sum_elements

class TestSumElements(unittest.TestCase):
    def test_sum_elements(self):
        self.assertEqual(sum_elements(['1', '2', '3', '4', '5']), 15)

if __name__ == '__main__':
    unittest.main()