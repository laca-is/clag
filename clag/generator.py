import jinja2
from os.path import dirname, join

def build_output_file(agents, envs, output_file):
    file_name = dirname(__file__)
    
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(join(file_name, "templates")),
        trim_blocks=True, lstrip_blocks=True
    )

    agent_jinja_template = jinja_env.get_template('agentTemplate.py.jinja')
    env_jinja_template = jinja_env.get_template('envTemplate.py.jinja')
    main_jinja_template = jinja_env.get_template('mainTemplate.py.jinja')
    
    with open(output_file, 'w') as f:
        f.write('from maspy import *\n\n')
        f.write(agent_jinja_template.render(agents=agents))
        f.write(env_jinja_template.render(envs=envs))
        f.write(main_jinja_template.render(agents=agents, envs=envs)) 