#!/usr/bin/env python3

from collections import defaultdict
import pathlib


def get_compl_strand(dna_strand_1):
    complimentary = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'T'}
    dna_strand_2 = ''
    n = len(dna_strand_1)
    for idx in range(n - 1, -1, -1):
        nuclio = dna_strand_1[idx]
        dna_strand_2 += complimentary[nuclio]
    return dna_strand_2


def main():
    in_data = ''
    current_dir = pathlib.Path(__file__).parent
    with open(f'{current_dir}/input.txt') as fp:
        in_data = fp.read()
    print(get_compl_strand(in_data))


if __name__ == "__main__":
    main()