import argparse

from .commands import build_commands


def main():
    parser = argparse.ArgumentParser(description='Vorteex CLI tool')
    parser.add_argument('--json', help='Output results in JSON')

    sub_parser_creator = parser.add_subparsers()
    build_commands(sub_parser_creator)

    args = parser.parse_args()
    args_dict = vars(args)

    if args.func:
        args.func(args_dict)


if __name__ == '__main__':
    main()
