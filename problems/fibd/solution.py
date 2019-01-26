#!/usr/bin/env python3

import pathlib
from pprint import pprint
from collections import defaultdict


def get_rabbit_pairs(alive_n, die_after_m):
    # die_after_n - die after n months
    # alive_m - all rabbits live for m months
    ages_amount = {1: 1}
    rabbit_amount = 1
    for month in range(1, alive_n):
        month_ages_amount = defaultdict(int)
        rabbit_amount = 0
        for item in ages_amount:
            if item == die_after_m:
                # if age of a pair is equal to <die_after_m> ->
                # then 1. pair will die and
                # 2. we will get only one pair of offsprint
                month_ages_amount[1] += ages_amount[item]
            elif item == 1:
                # if the pair of rabbit is small ->
                # we will 1. save the pair and
                # 2. will not get any offsprings
                month_ages_amount[item + 1] = ages_amount[item]
            elif item > 1:
                # if the pair of rabbit is big ->
                # we will 1. save the pair and
                # 2. will get offsprings
                month_ages_amount[item + 1] = ages_amount[item]
                month_ages_amount[1] += ages_amount[item]
        del ages_amount
        ages_amount = month_ages_amount

    rabbit_amount = 0
    for age in ages_amount:
        rabbit_amount += ages_amount[age]
    return rabbit_amount


def main():
    in_data = ''
    current_dir = pathlib.Path(__file__).parent
    with open(f'{current_dir}/input.txt') as fp:
        n, m = map(int, fp.read().split(' '))
    print(get_rabbit_pairs(n, m))


if __name__ == "__main__":
    main()