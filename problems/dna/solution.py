#!/usr/bin/env python3

from collections import defaultdict


def nucleo_stats(dna_seq):
    stats = defaultdict(int)
    for nuclio in dna_seq:
        stats[nuclio] += 1
    order_seq = ['A', 'C', 'G', 'T']
    return [stats[nuclio] for nuclio in order_seq]


def main():
    in_data = ''
    current_dir = pathlib.Path(__file__).parent
    with open(f'{current_dir}/input.txt') as fp:
        in_data = fp.read()
    print(' '.join(map(str, nucleo_stats(in_data))))


if __name__ == "__main__":
    main()