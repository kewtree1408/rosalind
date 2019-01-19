#!/usr/bin/env python3

try:
    from solution import rabbit_pairs
except ImportError:
    from .solution import rabbit_pairs

import unittest


class TestRabbitPairs(unittest.TestCase):
    def test_sample(self):
        months = 5
        k_pairs = 3
        result = 19
        assert rabbit_pairs(months, k_pairs) == result

    def test_ones(self):
        months = 1
        k_pairs = 1
        result = 1
        assert rabbit_pairs(months, k_pairs) == result

    def test_deafult_fib(self):
        months = 5
        k_pairs = 1
        result = 5
        assert rabbit_pairs(months, k_pairs) == result

    def test_real(self):
        months = 30
        k_pairs = 5
        result = 5164501096416
        assert rabbit_pairs(months, k_pairs) == result


if __name__ == '__main__':
    unittest.main()