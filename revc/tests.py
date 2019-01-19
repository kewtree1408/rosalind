#!/usr/bin/env python3

from solution import get_compl_strand
import unittest


class TestREVC(unittest.TestCase):
    def test_sample(self):
        dna_strand_1 = 'AAAACCCGGT'
        dna_strand_2 = 'ACCGGGTTTT'
        print(dna_strand_1, get_compl_strand(dna_strand_1), dna_strand_2)
        assert get_compl_strand(dna_strand_1) == dna_strand_2

    def test_empty(self):
        dna_strand_1 = ''
        dna_strand_2 = ''
        assert get_compl_strand(dna_strand_1) == dna_strand_2


if __name__ == '__main__':
    unittest.main()