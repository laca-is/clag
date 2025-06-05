import click
from clag import parse_file, build_output_file

@click.command
@click.argument('file_name', type=click.STRING)
@click.option('--output_file', '-o', default='out.py', help='Change output file name.')
@click.option('--debug', '-d', is_flag=True, help='Print clag debug information')
def build(file_name, output_file, debug):
    agents, envs = parse_file(file_name)
    # Debug printing
    if debug:
        for agent in agents:
            print('-------------------------------')
            print(f"Agent: {agent.name}")
            print(f"Beliefs: {agent.beliefs}")
            print(f"Desires: {agent.desires}")
            print(f"Channel: {agent.channel}")
            print(f"Environment: {agent.environment}")
            for plan in agent.plans:
                print(f"    Plan: {plan['name']}")
                print(f"    Conditions: {[c[1] for c in plan['conditions']]}")
                print(f"    Context: {plan['context']}")
                print(f"    Actions: {[a for a in plan['actions']]}")
        # Environment debug printing
        for env in envs:
            print('-------------------------------')
            print(f"Environment: {env.name}")
            print(f"Perceptions: {env.perceptions}")
            print(f"Actions: {env.actions}")
    build_output_file(agents, envs, output_file)