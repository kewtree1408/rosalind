#!/usr/bin/env python3

try:
    from solution import nucleo_stats
except ImportError:
    from .solution import nucleo_stats

import unittest


class TestDNA(unittest.TestCase):
    def test_sample(self):
        dna_seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
        # 'A', 'C', 'G', and 'T'
        result = [20, 12, 17, 21]
        assert nucleo_stats(dna_seq) == result

    def test_empty(self):
        dna_seq = ''
        # 'A', 'C', 'G', and 'T'
        result = [0, 0, 0, 0]
        assert nucleo_stats(dna_seq) == result


if __name__ == '__main__':
    unittest.main()