import hashlib
import json
import os
import shutil
import string
import subprocess

import utils

with open(utils.asset_path('ranges.json')) as f:
    default_ranges = json.load(f)

default_variation = {'variable': False, 'css': {}}


def optimise(config):
    # Check if destination is fine
    destination = os.path.abspath(config['output']['dir'])
    try:
        if not os.path.isdir(destination):
            os.makedirs(destination, exist_ok=True)
        if not os.access(destination, os.W_OK):
            raise Exception()
    except:
        print(f'Output directory not writable: "{destination}"')
        exit(1)

    # Clean
    if config['output']['clean']:
        print(f'Cleaning: "{destination}"')
        shutil.rmtree(destination)
        os.makedirs(destination)

    # Go over each font and variation of it.
    # Then go over every range and format and generate the subset
    # Finally add the relevant CSS

    css = ''
    with open(utils.asset_path('css.template')) as f:
        template = string.Template(f.read())
    for font, variations in config['fonts'].items():
        css += f'\n\n/* {font} */\n'
        for variation in variations:
            variation = utils.update_deep(default_variation, variation)
            print(f'Processing: {font} {os.path.basename(variation["file"])}')
            source = os.path.join(config['context'], variation['file'])
            for format in config['output']['formats']:
                for range, codes in default_ranges.items():
                    unicodes = ', '.join(codes)

                    # Create unique key on all parameters
                    key = font + variation['file'] + format + unicodes
                    key = hashlib.sha1(key.encode()).hexdigest()

                    # Generate subset
                    output_file = os.path.join(destination, f'{key}.{format}')
                    print(f'  {range}@{format} -> {output_file}')
                    command = f'pyftsubset --unicodes="{unicodes}" --layout-features="*" --flavor="{format}" --output-file="{output_file}" {source}'
                    subprocess.call(command, shell=True)

                    # Generate CSS
                    ending = format
                    if variation['variable']:
                        ending += '-variations'

                    src = f"url({config['output']['prefix']}{os.path.basename(output_file)}) format('{ending}')"
                    merged = utils.update_deep(
                        config['output']['css'], variation['css']
                    )
                    additional = '\n  '.join(
                        [f'{key}: {value};' for key, value in merged.items()]
                    )
                    css += template.substitute(
                        range=range,
                        font=font,
                        src=src,
                        unicodes=unicodes,
                        additional=additional,
                    )

    with open(os.path.join(destination, 'fonts.css'), 'w') as f:
        f.write(css.strip())
