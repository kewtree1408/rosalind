#!/usr/bin/env python3

import pathlib


def get_prob_of_dominant(k, m, n):
    # A - dominant factor
    # a - recessive factor
    # k - amount of organisms with AA factors (homozygous dominant)
    # m - amount of organisms with Aa factors (heterozygous)
    # n - amount of organisms with aa factors (homozygous recessive)
    events = ['AA+Aa', 'AA+aa', 'Aa+aa', 'AA+AA', 'Aa+Aa', 'aa+aa']

    # get the probability of dominant traits (set up Punnett square)
    punnett_probabilities = {
        'AA+Aa': 1,
        'AA+aa': 1,
        'Aa+aa': 1 / 2,
        'AA+AA': 1,
        'Aa+Aa': 3 / 4,
        'aa+aa': 0,
    }
    event_probabilities = {}
    totals = k + m + n

    # Event: AA+Aa -> P(X=k, Y=m) + P(X=m, Y=k):
    P_km = k / totals * m / (totals - 1)
    P_mk = m / totals * k / (totals - 1)
    event_probabilities['AA+Aa'] = P_km + P_mk

    # Event: AA+aa -> P(X=k, Y=n) + P(X=n, Y=k):
    P_kn = k / totals * n / (totals - 1)
    P_nk = n / totals * k / (totals - 1)
    event_probabilities['AA+aa'] = P_kn + P_nk

    # Event: Aa+aa -> P(X=m, Y=n) +P(X=n, Y=m):
    P_mn = m / totals * n / (totals - 1)
    P_nm = n / totals * m / (totals - 1)
    event_probabilities['Aa+aa'] = P_mn + P_nm

    # Event: AA+AA -> P(X=k, Y=k):
    P_kk = k / totals * (k - 1) / (totals - 1)
    event_probabilities['AA+AA'] = P_kk

    # Event: Aa+Aa -> P(X=m, Y=m):
    P_mm = m / totals * (m - 1) / (totals - 1)
    event_probabilities['Aa+Aa'] = P_mm

    # Event: aa+aa -> P(X=n, Y=n) + P(X=n, Y=n) = 0 (will be * 0, so just don't use it)
    event_probabilities['aa+aa'] = 0

    # Total probability is the sum of (prob of dominant factor * prob of the event)
    total_probability = 0
    for event in events:
        total_probability += punnett_probabilities[event] * event_probabilities[event]
    return round(total_probability, 5)


def main():
    in_data = ''
    current_dir = pathlib.Path(__file__).parent
    with open(f'{current_dir}/input.txt') as fp:
        k, m, n = map(int, fp.read().split(' '))
    print(get_prob_of_dominant(k, m, n))


if __name__ == "__main__":
    main()