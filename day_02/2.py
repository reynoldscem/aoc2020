from argparse import ArgumentParser
import re


def build_parser():
    parser = ArgumentParser()

    parser.add_argument('input_filename')

    return parser


def is_valid(line):
    pattern = r'^(\d+)-(\d+) (\w): (.*)$'
    match = re.match(pattern, line)
    character, password = match.groups()[2:]
    indices = (int(entry) - 1 for entry in match.groups()[:2])

    count = sum(password[index] == character for index in indices)

    return count == 1


def main():
    args = build_parser().parse_args()
    with open(args.input_filename) as fd:
        lines = fd.read().strip().splitlines()
    are_lines_valid = [is_valid(line) for line in lines]
    print(sum(are_lines_valid))


if __name__ == '__main__':
    main()
