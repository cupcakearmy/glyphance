import os

import click
import jsonschema
import yaml

import flags
import utils

default_config = {
    'output': {
        'dir': 'generated',
        'formats': ['woff2'],
        'prefix': '/',
        'css': {
            'font-display': 'swap',
            'font-style': 'normal',
            'font-weight': '400',
        },
        'clean': False,
    },
    "context": ".",
}


def validate(config):
    schema_file = utils.asset_path('config.schema.yaml')
    with open(schema_file, 'r') as f:
        schema = yaml.safe_load(f)
    return jsonschema.validate(config, schema)


def load(path):
    # Load config
    try:
        path = os.path.abspath(path)
        with open(path, 'r') as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        click.echo(f"Config file not found: {path}")
        exit(1)
    except yaml.YAMLError as e:
        click.echo(f"Config file is not valid YAML: {path}")
        click.echo(e)
        exit(1)

    # Setting dynamic defaults
    default_config['context'] = os.path.dirname(path)
    if flags.OUTPUT_DIRECTORY != None:
        default_config['output']['dir'] = flags.OUTPUT_DIRECTORY
    if flags.CLEAN != None:
        default_config['output']['clean'] = flags.CLEAN
    if flags.PREFIX != None:
        default_config['output']['prefix'] = flags.PREFIX

   # Merge defaults
    return utils.update_deep(default_config, config)
