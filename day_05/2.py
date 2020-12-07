from argparse import ArgumentParser
import numpy as np


def build_parser():
    parser = ArgumentParser()

    parser.add_argument('input_filename')

    return parser


def main():
    args = build_parser().parse_args()
    with open(args.input_filename) as fd:
        lines = fd.read().strip().splitlines()
    table = str.maketrans({'F': '0', 'B': '1', 'R': '1', 'L': '0'})

    all_ids = []
    for line in lines:
        binary_string = line.translate(table)
        decimal = int(binary_string, 2)
        all_ids.append(decimal)
    sorted_ids = sorted(all_ids)
    index_gap = np.where(np.diff(sorted_ids) == 2)[0][0]
    missing_seat = sorted_ids[index_gap] + 1
    print(missing_seat)


if __name__ == '__main__':
    main()
