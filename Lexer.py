import ply.lex as lex

#write code for bool,char

tokens = [
'INT',
'FLOAT',
'NAME',
'CHAR',
'PLUS',
'MINUS',
'DIVIDE',
'MULTIPLY',
'BOOL',
'EQUALS',
'STRING',
'LPAREN',
'RPAREN',
'PRINT',
'NUMBER',
'INT_t',
'FLOAT_t',
'BOOL_t',
'STRING_t',
'CHAR_t',
'EXP',
'PERCENT',
'PLUSPLUS',
'MINUSMINUS',
'GTHAN',
'LTHAN',
'GTHAN_EQ',
'LTHAN_EQ',
'NOT_EQ',
'EQ_EQ',
'COMMA',
'NOT',
'AND',
'OR',
'TRUE_t',
'FALSE_t',
'LIST',
'SQ_BR',
'SQ_BL',
'SLICE',
'DOT',
'PUSH',
'POP',
'INDEX',
'SEMI_C',
'FOR',
'CURL_l',
'CURL_r'
]
t_ignore = ' \n'
t_CURL_l=r'\{'
t_CURL_r=r'\}'
t_SEMI_C=r'\;'
t_DOT=r'\.'
t_SQ_BR=r'\]'
t_SQ_BL=r'\['
t_GTHAN=r'\>'
t_LTHAN=r'\<'
t_GTHAN_EQ=r'\>\='
t_LTHAN_EQ=r'\<\='
t_NOT_EQ=r'\!\='
t_EQ_EQ=r'\=\='
t_EXP=r'\^'
t_PERCENT=r'\%'
t_PLUSPLUS=r'\+\+'
t_MINUSMINUS=r'\-\-'
t_PLUS=r'\+'
t_MINUS=r'\-'
t_DIVIDE=r'\/'
t_MULTIPLY=r'\*'
t_EQUALS=r'\='
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_COMMA=r'\,'

def t_PUSH(t):
	r'push'
	return t

def t_FOR(t):
	r'for'
	return t


def t_POP(t):
	r'pop'
	return t

def t_INDEX(t):
	r'index'
	return t

def t_LIST(t):
	r'list'
	return t

def t_SLICE(t):
	r'slice'
	return t


def t_FLOAT(t):
	r'\d+\.\d+'
	t.value=float(t.value)
	return t

def t_TRUE_t(t):
	r'TRUE'
	return t

def t_FALSE_t(t):
	r'FALSE'
	return t

def t_INT(t):
	r'\d+'
	t.value=int(t.value)
	return t

def t_CHAR(t):
	r'\'[a-zA-Z0-9]{1}\''
	t.value=t.value[1:-1]
	return t

def t_NOT(t):
	r'NOT'
	return t

def t_AND(t):
	r'AND'
	return t

def t_OR(t):
	r'OR'
	return t


def t_NUMBER(t):
	r'-?[0-9]+(?:\.[0-9]*)?'
	t.value = float(t.value)
	return t

def t_PRINT(t):
	r'print'
	t.type='PRINT'
	return t

def t_BOOL(t):
    r'true|false'
    if(t.value=='true'or t.value=='1'):
        t.value=bool(t.value)
    else:
        t.value=not bool(t.value)
    return t

def t_INT_t(t):
	r'int'
	return t
def t_FLOAT_t(t):
	r'float'
	return t

def t_STRING_t(t):
	r'string'
	return t

def t_BOOL_t(t):
	r'bool'
	return t
def t_BTRUE(t):
	r'True'
	return t
def t_BFALSE(t):
	r'False'
	return t
def t_ZERO(t):
	r'0'
	return t
def t_ONE(t):
	r'1'
	return t

def t_CHAR_t(t):
	r'char'
	return t

def t_NAME(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type='NAME'
	return t
def t_STRING(t):
    r'"[^"\n]*"'
    t.value = t.value[1:-1]
    return t


def t_error(t):
	print("error in syntax")
	t.lexer.skip(1)



# while True:
# 	tok=lexer.token()
# 	if not tok:
# 		break
# 	print(tok)

