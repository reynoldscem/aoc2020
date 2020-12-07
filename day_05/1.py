from argparse import ArgumentParser


def build_parser():
    parser = ArgumentParser()

    parser.add_argument('input_filename')

    return parser


def main():
    args = build_parser().parse_args()
    with open(args.input_filename) as fd:
        lines = fd.read().strip().splitlines()
    table = str.maketrans({'F': '0', 'B': '1', 'R': '1', 'L': '0'})
    max_id = 0
    for line in lines:
        binary_string = line.translate(table)
        decimal = int(binary_string, 2)
        max_id = max(max_id, decimal)
    print(max_id)


if __name__ == '__main__':
    main()
