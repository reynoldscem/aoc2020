from argparse import ArgumentParser


def build_parser():
    parser = ArgumentParser()

    parser.add_argument('input_filename')

    return parser


def main():
    args = build_parser().parse_args()
    with open(args.input_filename) as fd:
        lines = fd.read().strip().splitlines()
    n_rows = len(lines)
    width = len(lines[0])

    down_slope, across_slope = (1, 3)
    position = (0, 0)
    tree_count = 0

    while position[0] < n_rows:
        tree_count += int(lines[position[0]][position[1] % width] == '#')
        position = (position[0] + down_slope, position[1] + across_slope)

    print(tree_count)


if __name__ == '__main__':
    main()
