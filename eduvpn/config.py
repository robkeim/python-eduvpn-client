from configparser import ConfigParser
from os import path

config_file = path.expanduser('~/.config/eduvpn')

defaults = {
    'discovery_uri': 'https://static.eduvpn.nl/',
    'key': 'E5On0JTtyUVZmcWd+I/FXRm32nSq8R2ioyW7dcu/U88=',
}


def read():
    config = ConfigParser()
    config['eduvpn'] = defaults
    config.read(config_file)
    return config


def write(config):
    with open(config_file, 'w') as f:
        config.write(f)

