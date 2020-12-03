from argparse import ArgumentParser
import re


def build_parser():
    parser = ArgumentParser()

    parser.add_argument('input_filename')

    return parser


def is_valid(line):
    pattern = r'^(\d+)-(\d+) (\w): (.*)$'
    match = re.match(pattern, line)
    lower_str, upper_str, character, password = match.groups()
    lower, upper = int(lower_str), int(upper_str)

    count = len(re.findall(character, password))

    return lower <= count and count <= upper


def main():
    args = build_parser().parse_args()
    with open(args.input_filename) as fd:
        lines = fd.read().strip().splitlines()
    are_lines_valid = [is_valid(line) for line in lines]
    print(sum(are_lines_valid))


if __name__ == '__main__':
    main()
