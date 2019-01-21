#!/usr/bin/env python3

try:
    from solution import get_prob_of_dominant
except ImportError:
    from .solution import get_prob_of_dominant

import unittest


class TestMendelLaw(unittest.TestCase):
    def test_sample(self):
        k = 2
        m = 2
        n = 2
        result = 0.78333
        assert get_prob_of_dominant(k, m, n) == result

    def test_all_from_k(self):
        k = 2
        m = 0
        n = 0
        result = 1
        assert get_prob_of_dominant(k, m, n) == result

    def test_all_from_m(self):
        k = 0
        m = 2
        n = 0
        result = 3 / 4
        assert get_prob_of_dominant(k, m, n) == result

    def test_all_from_n(self):
        k = 0
        m = 0
        n = 2
        result = 0
        assert get_prob_of_dominant(k, m, n) == result

    def test_1_from_k_1_from_m(self):
        k = 1
        m = 1
        n = 0
        result = 1
        assert get_prob_of_dominant(k, m, n) == result

    def test_1_from_k_1_from_n(self):
        k = 1
        m = 0
        n = 1
        result = 1
        assert get_prob_of_dominant(k, m, n) == result

    def test_1_from_m_1_from_n(self):
        k = 0
        m = 1
        n = 1
        result = 1 / 2
        assert get_prob_of_dominant(k, m, n) == result

    def test_real(self):
        k = 26
        m = 26
        n = 21
        result = 0.78529
        assert get_prob_of_dominant(k, m, n) == result


if __name__ == '__main__':
    unittest.main()