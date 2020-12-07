from argparse import ArgumentParser


def build_parser():
    parser = ArgumentParser()

    parser.add_argument('input_filename')

    return parser


def main():
    args = build_parser().parse_args()
    with open(args.input_filename) as fd:
        data = fd.read().strip()
    groups = data.split('\n\n')
    counts = [
        len(set(group.replace('\n', '')))
        for group in groups
    ]
    print(sum(counts))

if __name__ == '__main__':
    main()
