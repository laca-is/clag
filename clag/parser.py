from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
import click
from clag.antlr.ClagLexer import ClagLexer
from clag.antlr.ClagParser import ClagParser
from clag.error_handling import CustomErrorListener
from clag.listener import ClagListener

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