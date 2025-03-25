# File: main.py
import sys
from antlr4 import *
from MyLexer import MyLexer
from MyParser import MyParser
from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error at line {line}:{column} - {msg}")

def parse_file(filename):
    # 1. Read input file
    input_stream = FileStream(filename, encoding='utf-8')
    
    # 2. Create lexer and parser
    lexer = MyLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(CustomErrorListener())
    
    stream = CommonTokenStream(lexer)
    parser = MyParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())
    
    # 3. Start parsing from the 'system' rule
    parse_tree = parser.system()
    
    # 4. Print basic parse tree
    print("Parse Tree:")
    print(parse_tree.toStringTree(recog=parser))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py <input-file>")
        sys.exit(1)
    
    try:
        parse_file(sys.argv[1])
        print("Parsing completed successfully!")
    except Exception as e:
        print(e)