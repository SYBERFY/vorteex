def arguments(sub_parser_creator):
    query = sub_parser_creator.add_parser('query', help='Make a query')
    query.set_defaults(query=True, func=main)


def main(args):
    print('query')
