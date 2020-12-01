def arguments(sub_parser_creator):
    configure = sub_parser_creator.add_parser('configure', help='Configure API keys')
    configure.set_defaults(configure=True, func=main)


def main(args):
    print('configure')
