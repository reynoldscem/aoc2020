from argparse import ArgumentParser
import re


def build_parser():
    parser = ArgumentParser()

    parser.add_argument('input_filename')

    return parser


def parse_entry(entry_string):
    pairs = [pattern.split(':') for pattern in entry_string.split()]
    return dict(pairs)


def check_number(string, lower, upper):
    if not string.isnumeric():
        return False

    number = int(string)
    if number < lower or number > upper:
        return False

    return True


def entry_valid(entry):
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    field_intersection = set.intersection(required_keys, entry.keys())
    correct_fields = (len(field_intersection) == len(required_keys))
    if not correct_fields:
        return False

    if not check_number(entry['byr'], 1920, 2002):
        return False
    if not check_number(entry['iyr'], 2010, 2020):
        return False
    if not check_number(entry['eyr'], 2020, 2030):
        return False

    height = entry['hgt'][:-2]
    height_units = entry['hgt'][-2:]
    if not height.isnumeric():
        return False
    height = int(height)
    if height_units == 'cm':
        if height < 150 or height > 193:
            return False
    elif height_units == 'in':
        if height < 59 or height > 76:
            return False
    else:
        return False

    hair_colour = entry['hcl']
    if not re.match(r'^#[0-9a-f]{6}$', hair_colour):
        return False

    eye_colours = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    if entry['ecl'] not in eye_colours:
        return False

    if not re.match(r'^[0-9]{9}$', entry['pid']):
        return False

    return True


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
