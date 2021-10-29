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
    'COMMENT',
    'COMMENT_BLOCK',
    'STRING',
    'ID'
    ]

    reserved = {
        'if' : 'IF',
        'else' : 'ELSE',
        'while' : 'WHILE',
        'int'   : 'INT',
        'float' : 'FLOAT',
        'char'  : 'CHAR',
        'string': 'STRING_ID',
        'void' : 'VOID',
        'class' : 'CLASS',
        'static' : 'STATIC'
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

    # A regular expression rule with some action code
    def t_NUMBER(t):
        r'\d+'
        t.value = int(t.value)    
        return t

    # Define a rule so we can track line numbers
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'
    '''
    def t_identificador(t):
        r'([a-z]|[A-Z]|_|\.)([a-z]|[A-Z]|\d|_|\.)*'
        return t
    '''
    def t_STRING(t):
        r'\".*\"'
        return t

    def t_COMMENT(t):
        r'\/\/.*'
        return t

    def t_COMMENT_BLOCK(t):
        r'\/\*(.|\n)*\*\/'
        return t

    def t_ID(t):
        r'([a-z]|[A-Z]|_|\.)([a-z]|[A-Z]|\d|_|\.)*'
        t.type = reserved.get(t.value,'ID')    # Check for reserved words
        return t

    # Error handling rule
    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)    
        return t

    # Build the lexer
    lexer = lex.lex()
    
    f = open('fsharp.cs','r')
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
