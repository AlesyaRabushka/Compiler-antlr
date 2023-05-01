
from antlr4 import ParseTreeWalker
from antlr4 import *

from antlr4.tree import *
from MyGrammarLexer import MyGrammarLexer
from MyGrammarParser import MyGrammarParser
from MyGrammarListener import MyGrammarListener
from MyErrorListener import MyErrorListener

from KeyPrinter import KeyPrinter

if __name__ == '__main__':
    input = FileStream("example1")

    lexer = MyGrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)

    # parser.removeErrorListeners()
    # listener = MyErrorListener()
    # parser.addErrorListener(listener)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    # semantic analisys

    walker = ParseTreeWalker()
    printer = KeyPrinter()
    walker.walk(printer, tree)
