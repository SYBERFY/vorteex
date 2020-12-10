import os
from pathlib import Path
from configparser import ConfigParser


HOME = str(Path.home())
CONFIG_FOLDER = f'{HOME}/.vorteex'
CONFIG_FILE = f'{HOME}/.vorteex/config'


def exists():
    if os.path.exists(CONFIG_FILE):
        return True

    return False


def load():
    if not exists():
        return

    config_object = ConfigParser()
    config_object.read(CONFIG_FILE)

    return config_object


def write(section, key_value_pairs):
    config_object = load()

    if not config_object:
        config_object = ConfigParser()

        if not os.path.exists(CONFIG_FOLDER):
            os.mkdir(CONFIG_FOLDER)

    if section not in config_object:
        config_object[section] = {}

    for key, value in key_value_pairs.items():
        config_object[section][key] = value

    with open(CONFIG_FILE, 'w') as conf:
        config_object.write(conf)


def get_vorteex_api_key():
    config = load()

    if not config:
        return

    if 'settings' not in config:
        return

    return dict(config['settings']).get('api_key')


def get_all_sources():
    config = load()

    if not config:
        return

    if 'sources' not in config:
        return

    return dict(config['sources'])
