from unittest import TestCase, main
from proj.Date import change_date


class DateTest(TestCase):
    def test_date(self):
        self.assertEqual(change_date('2025-12-31'), ['31', '12', '2025'])


if __name__ == '__main__':
    main()