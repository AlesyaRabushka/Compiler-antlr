# Generated from MyGrammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammarParser#program.
    def enterProgram(self, ctx:MyGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#program.
    def exitProgram(self, ctx:MyGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#stat.
    def enterStat(self, ctx:MyGrammarParser.StatContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#stat.
    def exitStat(self, ctx:MyGrammarParser.StatContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#def.
    def enterDef(self, ctx:MyGrammarParser.DefContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#def.
    def exitDef(self, ctx:MyGrammarParser.DefContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#index.
    def enterIndex(self, ctx:MyGrammarParser.IndexContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#index.
    def exitIndex(self, ctx:MyGrammarParser.IndexContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#lists.
    def enterLists(self, ctx:MyGrammarParser.ListsContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#lists.
    def exitLists(self, ctx:MyGrammarParser.ListsContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#trees.
    def enterTrees(self, ctx:MyGrammarParser.TreesContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#trees.
    def exitTrees(self, ctx:MyGrammarParser.TreesContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#expr.
    def enterExpr(self, ctx:MyGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#expr.
    def exitExpr(self, ctx:MyGrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#func.
    def enterFunc(self, ctx:MyGrammarParser.FuncContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#func.
    def exitFunc(self, ctx:MyGrammarParser.FuncContext):
        pass



del MyGrammarParser