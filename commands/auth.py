import sys

from .. import prompt
from .. import config
from .. import utils


def arguments(sub_parser_creator):
    configure = sub_parser_creator.add_parser('auth', help='Associate to your Vorteex account')
    configure.set_defaults(configure=True, func=main)


def main(args):
    api_key = False
    has_account = prompt.confirm('Do you have a Vorteex account')

    if not has_account:
        wants_registration = prompt.confirm('Do you want to create one now')
        if not wants_registration:
            print('Bye then...')
            sys.exit(0)
        utils.open_browser('https://dashboard.vorteex.io/register')

    while not api_key:
        api_key = prompt.input(message='Insert Vorteex API Key')
        if api_key:
            break
        print('>>> Please input a valid API Key')

    config.write(section='settings', key_value_pairs={'api_key': api_key})
