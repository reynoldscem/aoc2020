from argparse import ArgumentParser
from itertools import product

def build_parser():
    parser = ArgumentParser()

    parser.add_argument('input_filename')

    return parser


def main():
    args = build_parser().parse_args()
    with open(args.input_filename) as fd:
        lines = fd.read().strip().splitlines()
    numbers = [int(number) for number in lines]
    for pair in product(numbers, numbers):
        pair_sum = sum(pair)
        if pair_sum == 2020:
            pair_product = pair[0] * pair[1]
            print(pair_product)
            break


if __name__ == '__main__':
    main()
