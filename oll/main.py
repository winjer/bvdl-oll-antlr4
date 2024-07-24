import sys
from antlr4 import *
from .OLLLexer import OLLLexer
from .OLLParser import OLLParser
from .visitor import Visitor


def main(argv):
    s = FileStream(sys.argv[1])
    lexer = OLLLexer(s)
    stream = CommonTokenStream(lexer)
    parser = OLLParser(stream)
    tree = parser.program()
    visitor = Visitor()
    visitor.visit(tree)
