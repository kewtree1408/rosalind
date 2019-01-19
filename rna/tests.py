#!/usr/bin/env python3

from solution import dna_to_rna
import unittest


class TestDNA(unittest.TestCase):
    def test_sample(self):
        dna_seq = 'GATGGAACTTGACTACGTAAATT'
        rna_seq = 'GAUGGAACUUGACUACGUAAAUU'
        assert dna_to_rna(dna_seq) == rna_seq

    def test_empty(self):
        dna_seq = ''
        rna_seq = ''
        assert dna_to_rna(dna_seq) == rna_seq


if __name__ == '__main__':
    unittest.main()