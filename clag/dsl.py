from antlr4 import *
import jinja2
import click
from os.path import dirname, join
import clag.filters
from clag.antlr.ClagLexer import ClagLexer
from clag.antlr.ClagParser import ClagParser
from clag.antlr.ClagParserListener import ClagParserListener
from antlr4.error.ErrorListener import ErrorListener

# Define data classes for agents/environments
class Agent:
    def __init__(self, name):
        self.name = name
        self.beliefs = []
        self.desires = []
        self.plans = []
        self.channel = None
        self.environment = None

class Environment:
    def __init__(self, name):
        self.name = name
        self.perceptions = []
        self.actions = []

file_name = dirname(__file__)

class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error at line {line}:{column} - {msg}")

class ClagListener(ClagParserListener):
    def __init__(self):
        self.agents = []
        self.envs = []
        self.current_agent = None
        self.current_env = None

    def enterAgentDef(self, ctx):
        self.current_agent = Agent(ctx.ID().getText())

    def exitAgentDef(self, ctx):
        self.agents.append(self.current_agent)
        self.current_agent = None

    def enterAgentSection(self, ctx):
        if ctx.BELIEVES():
            self.current_agent.beliefs = [t.getText() for t in ctx.idList().ID()]
        elif ctx.DESIRES():
            self.current_agent.desires = [t.getText() for t in ctx.idList().ID()]
        elif ctx.CHANNEL():
            self.current_agent.channel = ctx.getText()
        elif ctx.ENVIRONMENT():
            self.current_agent.environment = ctx.getText()

    def enterPlan(self, ctx):
        if self.current_agent:
            plan = {
                "name": ctx.ID().getText(),
                "conditions": [(c, c.ID().getText()) for c in ctx.conditionList().actionType()],
                "context": [(c, c.ID().getText()) for c in ctx.contextList().actionType()] if ctx.contextList() else [],
                "actions": [a.getText() for a in ctx.actionList().action()],
            }
            self.current_agent.plans.append(plan)

    def enterAction(self, ctx):
        if self.current_env:
            action = {
                "type": "send" if ctx.SEND() else "action",
                "details": ctx.getText()
            }
            self.current_env.actions.append(action)

    def enterEnvironmentSection(self, ctx):
        if self.current_env and ctx.THAT() and ctx.PERCEIVES():
            self.current_env.perceptions = [t.getText() for t in ctx.idList().ID()]

def parse_file(file):
    input_stream = FileStream(file)
    lexer = ClagLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ClagParser(stream)
    
    # Error handling
    error_listener = CustomErrorListener()
    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    parser.addErrorListener(error_listener)
    
    try:
        parse_tree = parser.system()
    except Exception as e:
        click.echo(f'[ERROR] {str(e)}')
        exit(1)
    
    listener = ClagListener()
    walker = ParseTreeWalker()
    walker.walk(listener, parse_tree)
    
    return (listener.agents, listener.envs)

def build_output_file(agents, envs, output_file):
    # Jinja setup remains similar to original
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(join(file_name, "templates")),
        trim_blocks=True, lstrip_blocks=True
    )

    jinja_env.filters.update({
        'dataType': clag.filters.data_type_to_str,
        'conditionsStr': clag.filters.conditions_to_str,
        'changeStr': clag.filters.change_to_srt
    })

    agent_jinja_template = jinja_env.get_template('agentTemplate.py.jinja')
    env_jinja_template = jinja_env.get_template('envTemplate.py.jinja')
    main_jinja_template = jinja_env.get_template('mainTemplate.py.jinja')
    with open(output_file, 'w') as f:
        f.write('from maspy import *\n')
        f.write(agent_jinja_template.render(agents=agents))
        f.write(env_jinja_template.render(envs=envs))
        f.write(main_jinja_template.render(agents=agents))