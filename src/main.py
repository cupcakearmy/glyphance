
import click

import cmd_optimise
import flags
from config import load, validate


@click.command()
@click.version_option("0.1.0")
@click.option('-v', '--verbose', is_flag=True, default=False, help="Run in verbose mode.")
@click.option('-c', '--config', type=click.Path(), required=True, help="Path to the config file.")
@click.option('-o', '--output-directory', type=click.Path(), help="Path to the output directory.")
@click.option('--clean', is_flag=True, help="Clean the output directory before generating.")
@click.option('--prefix', help="Prefix for the generated css font URLs.")
def cli(verbose, config, output_directory, clean, prefix):
    # Flags
    flags.VERBOSE = verbose
    if flags.VERBOSE:
        click.echo("Running in verbose mode.")
    flags.OUTPUT_DIRECTORY = output_directory
    flags.CLEAN = clean
    flags.PREFIX = prefix

    # Run
    c = load(config)
    validate(c)
    cmd_optimise.optimise(c)


if __name__ == '__main__':
    cli(auto_envvar_prefix="GLYPHANCE")
