import sys

from .. import prompt
from .. import config


def arguments(sub_parser_creator):
    configure = sub_parser_creator.add_parser('configure', help='Configure API keys')
    configure.set_defaults(configure=True, func=main)


def main(args):
    sources = config.get_all_sources()

    if sources:
        print('WARNING: You have previously configured API Keys, any overlapping source will be overwritten')

    sources = prompt.checkbox(
        message='Select the sources you wish to configure API keys for',
        choices=['Shodan', 'PassiveDNS', 'VirusTotal']
    )

    if len(sources) == 0:
        print('You must choose at least one source')
        sys.exit(1)

    configured_sources = {}
    for source in sources:
        api_key = prompt.input(
            message=f'{source} API Key',
        )

        if not api_key:
            continue

        configured_sources[source] = api_key

    if len(configured_sources) == 0:
        print('You must provide API keys for at least 1 source')
        sys.exit(1)

    config.write(section='sources', key_value_pairs=configured_sources)
    print('API Keys saved to ~/.vorteex/config')

    sys.exit(0)
