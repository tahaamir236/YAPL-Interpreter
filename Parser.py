import ply.yacc as yacc
import sys

#write code for bool char
tokens = [
'INT',
'FLOAT',
'STRING',
'CHAR',
'PLUS',
'MINUS',
'DIVIDE',
'MULTIPLY',
'BOOL',
'EQUALS',
'NAME',
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

precedence=(
	('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ_EQ','NOT_EQ'),
	('left','PLUS','MINUS'),
	('left','MULTIPLY','DIVIDE'),
	('left','EXP'),
	('right','NOT')
	)
def p_calc(p):
	'''
	calc : expression
	     | var_assign
	     | empty

	'''
	# print(run(p[1]))
	p[0] = p[1]


def p_var_assign(p):
	'''
	var_assign : INT_t NAME EQUALS expression
	           | FLOAT_t NAME EQUALS expression
	           | STRING_t NAME EQUALS expression
	           | BOOL_t NAME EQUALS expression
	           | CHAR_t NAME EQUALS expression
	'''
	p[0]=('=',p[1],p[2],p[4])


def p_expression_empty(p):
	'''
	expression : 
	'''
	p[0]=p[0]

# def p_expression_semicolon(p):
# 	'''
# 	expression : var_assign SEMI_C expression SEMI_C expression
# 	'''
# 	p[0]=(p[2],p[1],p[3],p[5])

def p_expression_FOR(p):
	'''
	expression : FOR lparen var_assign SEMI_C expression SEMI_C expression rparen CURL_l expression CURL_r
	'''
	p[0]=(p[1],p[3],p[5],p[7],p[10])

# def p_expression_plus(p):
# 	'''
# 	expression : NAME EQUALS NAME PLUS INT
# 	'''
# 	p[0]=('++',p[1])

# def p_expression_minus(p):
# 	'''
# 	expression : NAME EQUALS NAME MINUS INT
# 	'''
# 	p[0]=('--',p[1])


# def p_abc(p):
# 	'''
# 	var_assign : INT_t NAME EQUALS expression
# 	'''
def p_var_update(p):
	'''
	expression : NAME EQUALS expression

	'''
	p[0]=(',,',p[1],p[3])

# def p_var_update_second(p):
# 	'''
# 	expression : NAME EQUALS
# 	'''

def p_var_assign2(p):
	'''
	var_assign : INT_t NAME EQUALS lparen expression rparen
	           | FLOAT_t NAME EQUALS lparen expression rparen
	           | STRING_t NAME EQUALS lparen expression rparen
	           | BOOL_t NAME EQUALS lparen expression rparen
	           | CHAR_t NAME EQUALS lparen expression rparen
	'''
	p[0]=('=',p[1],p[2],p[5])


def p_list_expressions(p):
	'''
	expression : NAME DOT PUSH lparen expression rparen
			   | NAME DOT POP lparen expression rparen
			   | NAME DOT INDEX lparen expression rparen
	'''
	p[0]=(p[2],p[1],p[3],p[5])

def p_list_SQB(p):
	'''
	expression : NAME SQ_BL INT SQ_BR
	'''
	p[0]=('.',p[1],'index',p[3])

	
def p_expression_paranthesis(p):
	'''
	expression : lparen expression rparen
	'''
	p[0]=(p[2])

def p_lparen(p):
	'''
	lparen : LPAREN
	'''
	p[0]=p[1]

def p_rparen(p):
	'''
	rparen : RPAREN
	'''
	p[0]=p[1]



def p_expression(p):
	'''
	expression : expression PLUS expression
			   | expression MINUS expression
			   | expression MULTIPLY expression
			   | expression DIVIDE expression
			   | expression EXP expression
			   | expression PERCENT expression


	'''
	p[0]=(p[2],p[1],p[3])


# def p_not_exp(p):
# 	'''
# 	expression : NOT BOOL
# 			   | NOT NAME
# 	'''
# 	p[0]=('NOT',p[2])

# def p_logical_opperator(p):
# 	'''
# 	logical_operators : NOT
# 					  | AND
# 					  | OR
# 	'''
# 	p[0]=p[1]

def p_logical_expression(p):
	'''
	expression : NOT expression
	'''
	p[0]=(p[1],p[2])

def p_logical_expression_and_or(p):
	'''
	expression : expression AND expression
			   | expression OR expression
			   | expression EQ_EQ expression
			   | expression NOT_EQ expression
			   | expression LTHAN expression
			   | expression GTHAN expression
			   | expression GTHAN_EQ expression
			   | expression LTHAN_EQ expression
	'''
	p[0]=(p[2],p[1],p[3])


def p_expression_comma(p):
	'''
	expression : expression COMMA expression

	'''

	p[0]=(p[2],p[1],p[3])


def p_list_assign(p):
	'''
	var_assign : LIST NAME EQUALS SQ_BL expression SQ_BR
	'''
	p[0]=('list',p[2],p[5])

def p_expression_slice(p):
	'''
	expression : NAME DOT SLICE lparen expression COMMA expression rparen

	'''
	p[0]=(p[3],p[1],p[5],p[7])

def p_expression_PPMM(p):
	'''
	expression : expression PLUSPLUS
			   | expression MINUSMINUS
	'''
	p[0]=(p[2],p[1])

def p_print_from_env(p):
    '''
    expression : PRINT lparen NAME rparen
    '''
    p[0] = ('print_from_env', p[3])

def p_print_ex(p):
	'''
	expression : PRINT lparen expression rparen
	'''
	p[0]=(p[1],p[3])






def p_expression_int_float_char_bool_string(p):
	'''
	expression : INT
			   | FLOAT
			   | CHAR
			   | STRING
			   | BOOL

	'''
	p[0]=p[1]

def p_negative_assign(p):
	'''
	expression : MINUS INT
			   | MINUS FLOAT
	'''
	p[0]=-p[2]

# def p_minus_exp(p):
# 	'''
# 	expression : MINUS expression
# 	'''
# 	p[0]=-p[2]

def p_expression_var(p):
	'''
	expression : NAME
	'''
	p[0]=('var',p[1])


def p_var_assign_minus(p):
	'''
	expression : MINUS NAME
	'''
	p[0]=('var',p[1],p[2])


def p_empty(p):
	'''
	empty : 
	'''
	p[0]=None


def p_error(p):
	'''
	'''
	print('Syntax error!')

# parser=yacc.yacc()



# while True:
# 	try:
# 		s=input('')
# 	except EOFError:
# 		break
# 	parser.parse(s)




	