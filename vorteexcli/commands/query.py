import sys
import copy
import json

from .. import config
from ..api import API
from .. import output
from .. import utils


def arguments(sub_parser_creator):
    query = sub_parser_creator.add_parser('query', help='Make a query')

    group = query.add_mutually_exclusive_group(required=True)
    group.add_argument('-m', '--mode', help='Set query mode')
    group.add_argument('--available-modes', action='store_true', help='List available query modes based on configured sources')

    query.add_argument('-v', '--value', help='Set query value')
    query.set_defaults(query=True, func=main)

def print_available_modes(sources, available_modes):
    plural = 's' if len(sources) > 1 else ''
    print(f'These are the available modes based on the {len(sources)} source{plural} you have configured: ')

    for mode in available_modes:
        print(f'    - {mode}')


def main(args):
    findings = []
    special_modes = ['discover']
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

    api = API(authorization=api_key, sources=sources)
    global_module_map = api.get_global_module_map()
    global_module_map_filtered = utils.global_map_filter(global_module_map, from_point='category', to='source')
    available_modes = utils.determine_available_modes(global_module_map_filtered, sources) + special_modes

    if args['available_modes']:
        print_available_modes(sources, available_modes)
        sys.exit(0)

    if args['mode'] not in available_modes:
        print('Invalid mode, check available modes with: vorteex query --available-modes')
        sys.exit(1)

    if not args['value']:
        print('usage: vorteex query -m MODE --value VALUE\n')
        print('To perform a query you must provide a value')
        sys.exit(1)

    # resource == value == findable == asset
    resource = utils.determine_resource_type(args['value'])

    if not resource:
        print('The provided value does not appear to be a valid asset')
        sys.exit(1)

    iterable_global_module_map_filtered = copy.deepcopy(global_module_map_filtered)
    if args['mode'] != 'discover':
        for mode in iterable_global_module_map_filtered.keys():
            if args['mode'] == mode:
                global_module_map_filtered.pop(mode)

    source_resource = utils.extract_source_resources(global_module_map_filtered, available_modes, resource)

    if not source_resource:
        print(f"Could not find any configured source for the {resource} {args['value']}")
        sys.exit(0)

    categories = []
    sources = []
    for source, resources, category in source_resource:
        for res in resources:
            categories.append(category)
            sources.append(source)
            findings.append(api.make_query(source=source, resource=res, value=args['value']))

    findings = utils.aggregate_findings(findings)

    if args['json']:
        print(json.dumps(findings))
        sys.exit(0)

    output.human_readable(
        mode=args['mode'],
        resource=resource,
        findings=findings,
        categories=categories,
        sources=sources
    )

    sys.exit(0)
