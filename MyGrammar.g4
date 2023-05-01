//parser grammar ExprParser;
//options { tokenVocab=ExprLexer; }

grammar MyGrammar;

//parser grammar ParserGrammar;
program
    :  MAIN '{'stat*'}' EOF?
    ;

stat: TYPE? ID '=' expr ';'
    | expr ';'
    | TYPE ID ';'
    | def ';'
    | expr DOT expr ';'
    | TYPE? ID '=' expr DOT func ';'
    | RETURN expr ';'
    | TYPE ID (',' ID)* '='
        expr (',' expr)* ';'
    | ELSE '{'(stat)+'}' ';'
    | IF '('expr')'
        '{' (stat)+ '}'
      ELSE '{'(stat)+'}' ';'
    | IF '('expr')'
        '{' (stat)+ '}' ';'
    | WHILE '('expr')'
        '{'(stat)+ '}' ';'
    | SWITCH '('expr')''{'
        (CASE expr '{'(stat)*'}')+
        '}' ';'
    ;

def : TYPE ID '(' TYPE LINK ID
        (',' TYPE LINK ID)*')'
        '{' stat* '}' ;

index : '['INT']'
    | '['ID']';

lists: '[' INT (',' INT)* ']';

trees: '[' '['INT ',' INT ',' INT']' (',' '['INT ',' INT ',' INT']')* ';' '['INT ',' INT ',' INT']' (',' '['INT ',' INT ',' INT']')* ';' '['INT ',' INT ',' INT']' (',' '['INT ',' INT ',' INT']')* ']';

expr: ID
    | INT
    | func
    | 'not' expr
    | expr 'and' expr
    | expr 'or' expr
    | expr COMBINATION expr
    | expr INTERSECTION expr
    | expr SET expr
    | expr SSET expr
    | expr GREATER expr
    | expr LESS expr
    | expr INCREMENT
    | expr DECREMENT
    | lists
    | trees
    | expr index
    | INT+
    ;

func : ID '(' expr? (',' expr)* ')' ;




AND : 'and' ;
OR : 'or' ;
NOT : 'not' ;
EQ : '=' ;
GREATER: '>' ;
LESS: '<' ;
COMBINATION: '+' ;
INTERSECTION: '*' ;
SET: '-' ;
SSET: '/';
INCREMENT: '++' ;
DECREMENT: '--' ;
COMMA : ',' ;
SEMI : ';' ;
LPAREN : '(' ;
RPAREN : ')' ;
LCURLY : '{' ;
RCURLY : '}' ;
LSQUARE: '[' ;
RSQUARE: ']' ;
RETURN: 'return' ;
TYPE: 'int' | 'list' | 'element'| 'def'
    | 'queue' | 'tree' ;
LINK: '&' ;
DOT: '.' ;


IF: 'if' ;
ELSE: 'else' ;
WHILE: 'while' ;
SWITCH: 'switch' ;
CASE: 'case' ;
MAIN: 'main' ;


INT : [0-9]+ ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
WS: [ \t\n\r\f]+ -> skip ;
