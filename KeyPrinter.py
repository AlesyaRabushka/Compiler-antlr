from MyGrammarListener import MyGrammarListener
from antlr4.error.ErrorListener import ErrorListener
import sys

class KeyPrinter(MyGrammarListener, ErrorListener):
    def __init__(self):
        self.types_list = ['int', 'list', 'queue', 'element', 'tree']
        self.operators = ['++', '--', '>', '<']
        self.variables_list = []
        self.type_value_dict = {}
        # for DEF parametres
        self.buffer_pare = {}
        # for -- / ++ operators
        self.operator_pare = {}
        # dor IF / WHILE operators
        self.operator = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f'\nSemantic error occured at line <{line}>: {msg} {e}')
        sys.exit()

    # Enter a parse tree produced by MyGrammarParser#program.
    def enterProgram(self, ctx):
        pass

    # Exit a parse tree produced by MyGrammarParser#program.
    def exitProgram(self, ctx):
        print(self.variables_list)

    # Enter a parse tree produced by MyGrammarParser#stat.
    def enterStat(self, ctx):
        print('=== enter stat', ctx.getText())
        # print(ctx.getChildCount())
        # print(ctx.getChild(0, None).getText(), ctx.getChild(1, None).getText(),ctx.getChild(2, None).getText())

        # add all new variables into the list
        if ctx.getChild(0, None).getText() in self.types_list:
            # in case we have double initialization
            if ctx.getChild(2, None).getText() == ',':
                if ctx.getChild(1, None).getText() not in self.variables_list:
                    self.variables_list.append(ctx.getChild(1, None).getText())
                    self.type_value_dict[ctx.getChild(1, None).getText()] = ctx.getChild(0, None).getText()
                else:
                    self.syntaxError('p','f',f'{ctx.getText()} ','','value',f'<{ctx.getChild(1, None).getText()}> is already defined')
                if ctx.getChild(3, None).getText() not in self.variables_list:
                    self.variables_list.append(ctx.getChild(3, None).getText())
                    self.type_value_dict[ctx.getChild(3, None).getText()] = ctx.getChild(0, None).getText()
                else:
                    self.syntaxError('p', 'f', f'{ctx.getText()} ', '', 'value',
                                     f'<{ctx.getChild(3, None).getText()}> is already defined')

            # regular initialization
            else:
                if ctx.getChild(1, None).getText() not in self.variables_list:
                    self.variables_list.append(ctx.getChild(1, None).getText())
                    self.type_value_dict[ctx.getChild(1, None).getText()] = ctx.getChild(0, None).getText()
                else:
                    self.syntaxError('p','f',f'{ctx.getText()} ','','value',f'<{ctx.getChild(1, None).getText()}> is already defined')
        else:
            if 'def' in ctx.getChild(0, None).getText():
                pass

            # validation for IF / WHILE
            elif 'if' in  ctx.getChild(0, None).getText() or 'while' in  ctx.getChild(0, None).getText():
                self.operator = True

            # validation for SWITCH CASE
            elif 'switch' in ctx.getChild(0, None).getText():
                self.operator = True

            # validation for PRINT function
            elif 'print' in ctx.getChild(0, None).getText():
                pass

            # validation for -- and ++
            elif '--' in ctx.getChild(0, None).getText() or '++' in ctx.getChild(0, None).getText():
                value = ''
                for symbol in  ctx.getChild(0, None).getText():
                    if symbol != '-' and symbol != '+':
                        value += symbol
                if value not in self.variables_list:
                    self.syntaxError('p', 'f', f'{ctx.getText()} ', '', 'unknown value',
                                     f'<{value}>')

            else:
                # if variable is already in the list it's OK
                if ctx.getChild(0, None).getText() in self.variables_list:
                    for type in self.type_value_dict.keys():
                        if ctx.getChild(0, None).getText() == type:
                            # check for = operator
                            if ctx.getChild(1, None).getText() == '=':
                                # check for correct LIST's usage
                                if self.type_value_dict[type] == 'list' or self.type_value_dict[type] == 'tree':
                                    if ctx.getChild(2, None).getText() != '[':
                                        self.syntaxError('p','f',f'{ctx.getText()} ','','value',f'<{ctx.getChild(0, None).getText()}> has type <{self.type_value_dict[type]}>')

                                # check for correct QUEUE's usage
                                elif self.type_value_dict[type] == 'queue':
                                    print(ctx.getChild(2, None).getText())
                                    print( self.variables_list )
                                    if '+' in ctx.getChild(2, None).getText() or '-' in ctx.getChild(2, None).getText() or '/' in ctx.getChild(2, None).getText() or '*' in ctx.getChild(2, None).getText():
                                        self.operator = True
                                    elif ctx.getChild(2, None).getText() != '[' and ctx.getChild(2, None).getText() not in self.variables_list:
                                        self.syntaxError('p','f',f'{ctx.getText()} ','','value',f'<{ctx.getChild(0, None).getText()}> has type <{self.type_value_dict[type]}>')

                                    else:
                                        # check for QUEUE's MERGE function
                                        if 'merge' not in ctx.getChild(4, None).getText():
                                            self.syntaxError('p', 'f', f'{ctx.getText()} ', '', 'expected',
                                                             f'<merge> got <{ctx.getChild(4, None).getText()}>')
                                # check for correct ELEMENT's usage
                                elif self.type_value_dict[type] == 'element':
                                    if ctx.getChild(2, None).getText() not in '0123456789':
                                        self.syntaxError('p','f',f'{ctx.getText()} ','','value',f'<{ctx.getChild(0, None).getText()}> has type <{self.type_value_dict[type]}>')

                            # check for . operator
                            elif ctx.getChild(1, None).getText() == '.':
                                # check for LIST
                                if self.type_value_dict[type] == 'list':
                                    # check for LIST's APPEND function
                                    if 'append' not in ctx.getChild(2, None).getText():
                                        self.syntaxError('p', 'f', f'{ctx.getText()} ', '', 'expected',f'<append> got <{ctx.getChild(2, None).getText()}>')

                                # check for TREE
                                elif self.type_value_dict[type] == 'tree':
                                    # check for TREE's BALANCE function
                                    if 'balance' not in ctx.getChild(2, None).getText():
                                        self.syntaxError('p', 'f', f'{ctx.getText()} ', '', 'expected',f'<balance> got <{ctx.getChild(2, None).getText()}>')

                # check for RETURN
                elif ctx.getChild(0, None).getText() == 'return':
                    print(ctx.getChild(1, None).getText())
                    if ctx.getChild(1, None).getText() in self.variables_list:
                        pass
                    else:
                        self.syntaxError('p', 'f', f'{ctx.getText()} ', '', 'unknown value',
                                         f'<{ctx.getChild(1, None).getText()}>')

                # if we catch the variable, but it is not in the list -> ERROR
                elif ctx.getChild(0, None).getText() not in self.types_list or  ctx.getChild(0, None).getText() not in self.variables_list:
                    # print(f'ERROR in {ctx.getChild(0, None).getText()}')
                    self.syntaxError('p','f',f'{ctx.getText()} ','','unknown value',f'<{ctx.getChild(0, None).getText()}>')




    # Exit a parse tree produced by MyGrammarParser#stat.
    def exitStat(self, ctx):
        pass

    # Enter a parse tree produced by MyGrammarParser#def.
    def enterDef(self, ctx):
        # add PARAMETR's type and variable for valid semantic analisys
        self.type_value_dict[ctx.getChild(5, None).getText()] = ctx.getChild(3, None).getText()
        self.variables_list.append(ctx.getChild(5, None).getText())
        self.buffer_pare[ctx.getChild(5, None).getText()] = ctx.getChild(3, None).getText()
        # check for the TYPE
        if ctx.getChild(3, None).getText() not in self.types_list:
            self.syntaxError('p','f',f'{ctx.getText()} ','','expected TYPE got ',f'{ctx.getChild(3, None).getText()}')

        # check for the & symbol
        elif ctx.getChild(4, None).getText() != '&':
            self.syntaxError('p','f',f'{ctx.getText()} ','','expected & got ',f'{ctx.getChild(4, None).getText()}')




    # Exit a parse tree produced by MyGrammarParser#def.
    def exitDef(self, ctx):
        print(ctx.getChild(5, None).getText())
        for key in self.buffer_pare.keys():
            print(key)
            self.type_value_dict.pop(key)
            self.variables_list.remove(key)
        self.buffer_pare = {}

    # Enter a parse tree produced by MyGrammarParser#index.
    def enterIndex(self, ctx):
        pass

    # Exit a parse tree produced by MyGrammarParser#index.
    def exitIndex(self, ctx):
        pass

    # Enter a parse tree produced by MyGrammarParser#lists.
    def enterLists(self, ctx):
        # print('enter list', ctx.getText())
        pass

    # Exit a parse tree produced by MyGrammarParser#lists.
    def exitLists(self, ctx):
        pass

    # Enter a parse tree produced by MyGrammarParser#trees.
    def enterTrees(self, ctx):
        pass

    # Exit a parse tree produced by MyGrammarParser#trees.
    def exitTrees(self, ctx):
        pass

    # Enter a parse tree produced by MyGrammarParser#expr.
    def enterExpr(self, ctx):
        print('=== enter expr', ctx.getChild(0, None).getText(),ctx.getChildCount())
        if (self.operator):
            self.operator = False
            if ctx.getChild(0, None).getText() not in self.variables_list and ctx.getChild(0, None).getText() not in '0123456789':

                self.syntaxError('p', 'f', f'{ctx.getText()} ', '', 'unknown value',
                                 f'<{ctx.getChild(0, None).getText()}>')

        # if ctx.getChild(0, None).getText():
        #     if ctx.getChild(0, None).getText() not in self.variables_list and ctx.getChild(0, None).getText() not in self.types_list and ctx.getChild(0, None).getText() not in self.operators:
        #         self.syntaxError('p','f',f'{ctx.getText()} ','','unknown value',f'<{ctx.getChild(0, None).getText()}>')
        # print(ctx.getChild(0, None).getText())

    # Exit a parse tree produced by MyGrammarParser#expr.
    def exitExpr(self, ctx):
        pass

    # Enter a parse tree produced by MyGrammarParser#func.
    def enterFunc(self, ctx):
        pass

    # Exit a parse tree produced by MyGrammarParser#func.
    def exitFunc(self, ctx):
        pass