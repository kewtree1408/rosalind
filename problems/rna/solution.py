#!/usr/bin/env python3

from collections import defaultdict
import pathlib


def dna_to_rna(dna_seq):
    return dna_seq.replace('T', 'U')


def main():
    in_data = ''
    current_dir = pathlib.Path(__file__).parent
    with open(f'{current_dir}/input.txt') as fp:
        in_data = fp.read()
    print(dna_to_rna(in_data))


if __name__ == "__main__":
    main()