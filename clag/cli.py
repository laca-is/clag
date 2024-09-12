import click

import clag.dsl

@click.group
def run():
    pass

@run.command
@click.argument('file_name', type=click.STRING)
@click.option('--output_file', '-o', default='out.py', help='Change output file name.')
def build(file_name, output_file):
    agents, envs = clag.dsl.parse_file(file_name)
    clag.dsl.build_output_file(agents, envs, output_file)
    
# debug purposes
if __name__ == '__main__':
    run()