#!/usr/bin/env python3

from collections import defaultdict
import pathlib


def rabbit_pairs(months, k_pairs):
    if months <= 2:
        return 1

    small_pairs = 0
    big_pairs = 1

    small_pairs_prev = 0
    big_pairs_prev = 1

    for i in range(months - 2):
        small_pairs = big_pairs_prev * k_pairs
        big_pairs = big_pairs_prev + small_pairs_prev

        small_pairs_prev = small_pairs
        big_pairs_prev = big_pairs

    return small_pairs + big_pairs


def main():
    in_data = ''
    current_dir = pathlib.Path(__file__).parent
    with open(f'{current_dir}/input.txt') as fp:
        months, k_pairs = map(int, fp.read().split(' '))
    print(rabbit_pairs(months, k_pairs))


if __name__ == "__main__":
    main()