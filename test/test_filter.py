import unittest

from ney.filter import *


class FilterTestCase(unittest.TestCase):

    def test_never_matching_filter(self):
        test_filter = NeverMatchingFilter()
        self.assertEqual(test_filter.number_of_checks, 0)
        self.assertEqual(test_filter.number_of_matches, 0)
        self.assertFalse(test_filter.is_matched(''))
        self.assertEqual(test_filter.number_of_checks, 1)
        self.assertEqual(test_filter.number_of_matches, 0)

    def test_always_matching_filter(self):
        test_filter = AlwaysMatchingFilter()
        self.assertEqual(test_filter.number_of_checks, 0)
        self.assertEqual(test_filter.number_of_matches, 0)
        self.assertTrue(test_filter.is_matched(''))
        self.assertEqual(test_filter.number_of_checks, 1)
        self.assertEqual(test_filter.number_of_matches, 1)

    def test_regex_filter(self):
        test_filter = RegexFilter(r'.*bad.*')
        self.assertTrue(test_filter.is_matched('This message is bad.'))
        self.assertFalse(test_filter.is_matched('This message is good.'))
        self.assertEqual(test_filter.number_of_checks, 2)
        self.assertEqual(test_filter.number_of_matches, 1)


if __name__ == '__main__':
    unittest.main()
