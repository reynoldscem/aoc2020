from argparse import ArgumentParser


def build_parser():
    parser = ArgumentParser()

    parser.add_argument('input_filename')

    return parser


def parse_entry(entry_string):
    pairs = [pattern.split(':') for pattern in entry_string.split()]
    return dict(pairs)


def entry_valid(entry):
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return len(set.intersection(required_keys, entry.keys())) == len(required_keys)


def main():
    args = build_parser().parse_args()
    with open(args.input_filename) as fd:
        data = fd.read().strip()
    entry_strings = data.split('\n\n')
    entries = [parse_entry(string) for string in entry_strings]

    valid_entries = [entry for entry in entries if entry_valid(entry)]
    print(len(valid_entries))


if __name__ == '__main__':
    main()
