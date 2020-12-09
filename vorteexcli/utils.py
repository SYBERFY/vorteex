import sys
import subprocess

import validators


def open_browser(link):
    if sys.platform == 'win32':
        subprocess.Popen(['start', link], shell=True)

    elif sys.platform == 'darwin':
        subprocess.Popen(['open', link])

    else:
        try:
            subprocess.Popen(['xdg-open', link])
        except OSError:
            print(f'Go to: {link}')


def global_map_filter(global_map, from_point, to):
    result = {}

    if from_point == 'findable' and to == 'source':
        for source_name, source_content in global_map.items():
            for resource_name, resource_content in source_content.items():
                for findable_name, findable_content in resource_content.items():
                    if findable_name not in result:
                        result[findable_name] = {}

                    if source_name not in result[findable_name]:
                        result[findable_name][source_name] = []

                    result[findable_name][source_name].append(resource_name)

    elif from_point == 'category' and to == 'source':
        for source_name, source_content in global_map.items():
            for resource_name, resource_content in source_content.items():
                for findable_name, findable_content in resource_content.items():
                    for category in findable_content['categories']:
                        if category not in result:
                            result[category] = {}

                        if findable_name not in result[category]:
                            result[category][findable_name] = {}

                        if source_name not in result[category][findable_name]:
                            result[category][findable_name][source_name] = []

                        result[category][findable_name][source_name].append(resource_name)

    else:
        print('No filtered map view for parameters-> from: {from_point}, to: {to}')

    return result


def determine_resource_type(value):
    if validators.ipv4(value) or validators.ipv6(value):
        return 'ip'

    if validators.domain(value):
        return 'domain'

    if validators.email(value):
        return 'email'

    if validators.mac_address(value):
        return 'mac_address'


def determine_available_modes(inverted_global_map, api_keys):
    result = []

    for category in inverted_global_map.keys():
        for findable in inverted_global_map[category].keys():
            for source in inverted_global_map[category][findable].keys():
                if api_keys.get(source):
                    result.append(category)

    return result


def extract_source_resources(inverted_global_map, available_modes, resource):
    result = []

    for category in inverted_global_map.keys():
        if category not in available_modes:
            continue

        for findable in inverted_global_map[category].keys():
            if findable != resource:
                continue

            for source, resources in inverted_global_map[category][findable].items():
                result.append((source, resources, category))

    return result


def aggregate_findings(finding_list):
    result = {}

    for findings in finding_list:
        for findable in findings.keys():
            if findable not in result:
                result[findable] = []

            for f in findings[findable]:
                result[findable].append(f)

    return result
