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
    for triple in product(numbers, numbers, numbers):
        triple_sum = sum(triple)
        if triple_sum == 2020:
            triple_product = triple[0] * triple[1] * triple[2]
            print(triple_product)
            break


if __name__ == '__main__':
    main()
