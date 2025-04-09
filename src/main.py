import click
import jsonschema

import cmd_optimise
import flags
from config import load, validate


@click.command()
@click.version_option('1.0.0')
@click.option(
    '-v', '--verbose', is_flag=True, default=False, help='Run in verbose mode.'
)
@click.option(
    '-c', '--config', type=click.Path(), required=True, help='Path to the config file.'
)
@click.option(
    '-o', '--output-directory', type=click.Path(), help='Path to the output directory.'
)
@click.option(
    '--clean', is_flag=True, help='Clean the output directory before generating.'
)
@click.option('--prefix', help='Prefix for the generated css font URLs.')
def cli(verbose, config, output_directory, clean, prefix):
    # Flags
    flags.VERBOSE = verbose
    if flags.VERBOSE:
        click.echo('Running in verbose mode.')
    flags.OUTPUT_DIRECTORY = output_directory
    flags.CLEAN = clean
    flags.PREFIX = prefix

    # Run
    c = load(config)
    try:
        validate(c)
    except jsonschema.exceptions.ValidationError as e:
        click.echo('Config validation failed:')
        click.echo(f'{e.message} @ {e.json_path}')
        exit(1)
    cmd_optimise.optimise(c)


if __name__ == '__main__':
    cli(auto_envvar_prefix='GLYPHANCE')
