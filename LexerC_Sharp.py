# ------------------------------------------------------------
# Lexer para C#
# ------------------------------------------------------------
import ply.lex as lex
from tabulate import tabulate

def main():
    # List of token names.   This is always required
    tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'START_BLOCK',
    'END_BLOCK',
    'END_INSTRUCTION',
    'ASSIGN',
    'EQUAL',
    'GREATER_THAN',
    'GREATER_OR_EQUAL',
    'LESS_THAN',
    'LESS_OR_EQUAL',
    'COMMENT',
    'COMMENT_BLOCK',
    'STRING',
    'IDENTIFIER'
    ]

    reserved = {
        'if' : 'IF',
        'else' : 'ELSE',
        'while' : 'WHILE',
        'int'   : 'INT',
        'double' : 'DOUBLE',
        'char'  : 'CHAR',
        'string': 'STRING_ID',
        'void' : 'VOID',
        'class' : 'CLASS',
        'static' : 'STATIC',
        'public' : 'PUBLIC'
    }

    tokens = tokens + list(reserved.values())

    # Regular expression rules for simple tokens
    t_PLUS    = r'\+'
    t_MINUS   = r'-'
    t_TIMES   = r'\*'
    t_DIVIDE  = r'/'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_START_BLOCK = r'\{'
    t_END_BLOCK = r'\}'
    t_END_INSTRUCTION = r'\;'
    t_ASSIGN = r'\='
    t_EQUAL = r'\=\='
    t_GREATER_THAN = r'\>'
    t_GREATER_OR_EQUAL = r'\>\='
    t_LESS_THAN = r'\<'
    t_LESS_OR_EQUAL = r'\<\='

    def t_NUMBER(t):
        r'[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)'
        try:
            t.value = int(t.value)
        except:
            t.value = float(t.value)
           
        return t

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore  = ' \t'

    def t_STRING(t):
        r'\".*\"'
        return t

    def t_COMMENT(t):
        r'\/\/.*'
        return t

    def t_COMMENT_BLOCK(t):
        r'\/\*(.|\n)*\*\/'
        return t

    def t_IDENTIFIER(t):
        r'([a-z]|[A-Z]|_|\.)([a-z]|[A-Z]|\d|_|\.)*'
        t.type = reserved.get(t.value,'IDENTIFIER') 
        return t

    # Error handling rule
    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)    
        return t

    # Build the lexer
    lexer = lex.lex()
    
    f = open('fsharp.cs','r')
    #f = open('fsharp02.cs','r') //Ejemplo 2
    lexer.input(f.read())

    data=[]
 
    while True:
        tok=lexer.token()
        if not tok:
            break
        data.append([tok.type, tok.value, tok.lineno])
    print(tabulate(data, headers = ["Type","Value","#Line"]))
   
if __name__ == '__main__':
    main()  
