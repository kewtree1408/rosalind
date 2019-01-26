#!/usr/bin/env python3

try:
    from solution import get_rabbit_pairs
except ImportError:
    from .solution import get_rabbit_pairs

import unittest


class TestRabbitPairs(unittest.TestCase):
    def test_sample(self):
        n = 6
        m = 3
        result = 4
        assert get_rabbit_pairs(n, m) == result

    def test_with_ones(self):
        n = 1
        m = 1
        result = 1
        assert get_rabbit_pairs(n, m) == result

    def test_die_after_1_month(self):
        n = 100
        m = 1
        result = 1
        assert get_rabbit_pairs(n, m) == result

    def test_max_values(self):
        n = 100
        m = 20
        result = 353368918335207375428
        assert get_rabbit_pairs(n, m) == result

    def test_first_attempt(self):
        n = 93
        m = 19
        result = 12155974612912572979
        assert get_rabbit_pairs(n, m) == result


if __name__ == '__main__':
    unittest.main()