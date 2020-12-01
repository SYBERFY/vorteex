import sys

from .. import config


def arguments(sub_parser_creator):
    query = sub_parser_creator.add_parser('query', help='Make a query')
    query.add_argument('-m', '--mode', help='Query mode')
    query.add_argument('--available-modes', help='Query mode')
    query.set_defaults(query=True, func=main)


def main(args):
    api_key = config.get_vorteex_api_key()
    sources = config.get_all_sources()

    if not api_key:
        print('You must be authenticated to perform queries')
        print('Please run: vorteex auth')
        sys.exit(1)

    if not sources:
        print('No sources available to query from')
        print('Please run: vorteex configure')
        sys.exit(1)

    sys.exit(0)
