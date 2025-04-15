import os
from configparser import ConfigParser


def load_config(filename='database.ini', section='postgresql') -> dict:
    config_directory = os.path.dirname(__file__)
    filename = config_directory + '\\' + filename

    parser = ConfigParser()
    parser.read(filename)

    config = dict()
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    return config


DB_CONFIG = load_config('database.ini', 'postgresql')

