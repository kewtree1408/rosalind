#!/usr/bin/env python3

# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective
# number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

from collections import defaultdict


def nucleo_stats(dna_seq):
    stats = defaultdict(int)
    for nuclio in dna_seq:
        stats[nuclio] += 1
    order_seq = ['A', 'C', 'G', 'T']
    return [stats[nuclio] for nuclio in order_seq]


def main():
    in_data = ''
    with open('input.txt') as fp:
        in_data = fp.read()
    print(' '.join(map(str, nucleo_stats(in_data))))


if __name__ == "__main__":
    main()