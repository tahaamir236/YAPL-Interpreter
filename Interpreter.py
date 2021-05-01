import Lexer 
import Parser
import ply.lex as lex
import ply.yacc as yacc
import sys

global env
env = {}
result = False

global str_dict
global int_dict
global flt_dict
global char_dict
global bool_dict
str_dict={}
int_dict={}
flt_dict={}
char_dict={}
bool_dict={}
global x
x=0
def run(p):
	if type(p)==tuple:
		if p[0]=='+':
			t1=run(p[1])
			t2=run(p[2])
			if type(t1)==str and type(t2)==str:
				return t1+t2
			else:
				if type(t1)!=type(t2):
					if (type(t1)==int or type(t1)==float) and (type(t2)==int or type(t2)==float):
						return t1+t2
					else:
						sys.exit("Type Error")
				else:
					return t1+t2
		elif p[0]=='^':
			return run(p[1])**run(p[2])
		elif p[0]=='list':
			list_val = run(p[2])
			if p[1] not in env:
				if list_val == None:
					temp_list = []
					env[p[1]]= temp_list
				else:
					list1=[]
					list1=list_val
					final_l=[]
					while (type(list1)==list):
						temp=list1[0]
						final_l.append(temp)
						list1=list1.pop()
					final_l.append(list1)
					env[p[1]]=final_l
			else:
				print("variable already used")
		elif p[0]==',,':
			if p[1] in env:
				temp=run(p[2])
				if type(env[p[1]])==type(temp):
					env[p[1]]=temp

				else:
					sys.exit("Type Error")
			else:
				print("undeclared variable")
		elif p[0]=='for':
			t1=run(p[1])
			while run(p[2]):
				run(p[4])
				run(p[3])
			del env[p[1][2]]		

			# for x in range(t1):
			# 	if t2==True:
			# 		print("abc")
			# 		t2=run(p[2])
		elif p[0]=='.':
			if p[1] in env and type(env[p[1]])==list:
				if p[2]=='push':
					temp=env[p[1]]
					temp.append(p[3])
					env[p[1]]=temp

				elif p[2]=='pop':
					temp2=env[p[1]]
					list_len=len(temp2)-1
					input_len=p[3]
					if type(p[3])==int and input_len<=list_len:
						# temp=env[p[1]]
						# p_value=temp.pop(p[3])
						# # env[p[1]]=temp
			
						# return p_value
						temp=env[p[1]]
						temp3=temp.pop(p[3])
						return temp3
					else:
						sys.exit("index not int/range out of bounds")
						
				elif p[2]=='index':
					list_len=len(env[p[1]])-1
					input_len=p[3]
					if type(p[3])==int and input_len<=list_len:
						temp=env[p[1]]
						temp2=temp[p[3]]
						return temp2
					else:
						sys.exit("index not int/range out of bounds")
						
			else:
				print("list does not exists")
		elif p[0]=='slice':
			if p[1] in env and type(env[p[1]])==list:
				temp=len(env[p[1]])
				# print(temp)
				if type(p[2])==int and type(p[3])==int:
					if (p[2]>temp or p[2]<0) or p[3]>temp:
						sys.exit("index not int/range out of bounds")
					else:
						a=p[2]
						b=p[3]
						temp2=[]
						temp2=env[p[1]]
						temp3=[]
						for x in range(a,b):
							temp3.append(temp2[x])
						print(temp3)
				else:
					sys.exit("Type Error")	
			else:
				print("Variable error")
		elif p[0]=='NOT':
			temp=run(p[1])
			if type(temp) == bool: 
				return not(temp)
			else:
				sys.exit("Type Error")
		elif p[0]=='AND':
			t1=run(p[1])
			t2=run(p[2])
			if type(t1)==bool and type(t2)==bool:
				return t1 and t2
			else:
				sys.exit("Type Error")
		elif p[0]=='OR':
			t1=run(p[1])
			t2=run(p[2])
			if type(t1)==bool and type(t2)==bool:
				return t1 or t2
			else:
				sys.exit("Type Error")
		elif p[0]=='==':
			t1=run(p[1])
			t2=run(p[2])
			if type(t1)==type(t2):
				if t1==t2:
					return True
				else:
					return False
			elif t1==True and t2==1:
				return True
			elif t1==True and t2==0:
				return False
			elif t1==False and t2==0:
				return True
			elif t1==False and t2==1:
				return False
			else:
				sys.exit("Type Error")
		elif p[0]=='!=':
			t1=run(p[1])
			t2=run(p[2])
			if type(t1)==type(t2):
				if t1!=t2:
					return True
				else:
					return False
			elif t1==True and t2==1:
				return False
			elif t1==True and t2==0:
				return True
			elif t1==False and t2==0:
				return False
			elif t1==False and t2==1:
				return True
			else:
				sys.exit("Type Error")
		elif p[0]=='<':
			t1=run(p[1])
			t2=run(p[2])
			if (type(t1)==int and type(t2)==int) or (type(t1)==float and type(t2)==float):
				if t1<t2:
					return True
				else:
					return False
			else:
				sys.exit("Type Error")
		elif p[0]=='>':
			t1=run(p[1])
			t2=run(p[2])
			if (type(t1)==int and type(t2)==int) or (type(t1)==float and type(t2)==float):
				if t1>t2:
					return True
				else:
					return False
			else:
				sys.exit("Type Error")
		elif p[0]=='<=':
			t1=run(p[1])
			t2=run(p[2])
			if (type(t1)==int and type(t2)==int) or (type(t1)==float and type(t2)==float):
				if t1<t2 or t1==t2:
					return True
				else:
					return False
			else:
				sys.exit("Type Error")
		elif p[0]=='>=':
			t1=run(p[1])
			t2=run(p[2])
			if (type(t1)==int and type(t2)==int) or (type(t1)==float and type(t2)==float):
				if t1>t2 or t1==t2:
					return True
				else:
					return False
			else:
				sys.exit("Type Error")
		elif p[0]=='%':
			return run(p[1])%run(p[2])
		elif p[0]==',':
			# if p[3]=='print':
			# 	return str(run(p[1]))+" "+str(run(p[2]))
			# else:
			list1=[]
			list1.append(run(p[1]))
			list1.append(run(p[2]))
			return list1
		elif p[0]=="++":
			if p[1][1] in env:
				if p[1][1] in int_dict:
					int_dict[p[1][1]]=int_dict[p[1][1]]+1
					env[p[1][1]]=env[p[1][1]]+1

				elif p[1][1] in flt_dict:
					flt_dict[p[1][1]]=flt_dict[p[1][1]]+1
					env[p[1][1]]=env[p[1][1]]+1

				else:
					sys.exit("Type Error")
			else:
				print("variable not found")
		elif p[0]=='--':
			if p[1][1] in env:
				if p[1][1] in int_dict:
					int_dict[p[1][1]]=int_dict[p[1][1]]-1
					env[p[1][1]]=env[p[1][1]]-1

				elif p[1][1] in flt_dict:
					flt_dict[p[1][1]]=flt_dict[p[1][1]]-1
					env[p[1][1]]=env[p[1][1]]-1

				else:
					sys.exit("Type Error")
			else:
				print("variable not found")
		elif p[0]=='-':
			return run(p[1])-run(p[2])
		elif p[0]=='/':
			return run(p[1])/run(p[2])
		elif p[0]=='*':
			return run(p[1])*run(p[2])
		elif p[0]=='=':
			temp=run(p[3])
			if p[1]=="int" and type(temp)==int:
				if p[2] in env:
					print("Redeclaration Error")
				else:
					int_dict[p[2]]=temp
					env[p[2]]=temp

			elif p[1]=="float"and type(temp)==float:
				if p[2] in env:
					print("Redeclaration Error")
				else:
					flt_dict[p[2]]=temp
					env[p[2]]=temp

			elif p[1]=='string'and type(temp)==str:
				if p[2] in env:
					print("Redeclaration Error")
				else:
					str_dict[p[2]]=temp
					# env[p[2]]=(run(p[3]))
					env[p[2]]=temp

			elif p[1]=='bool' and (type(temp)==bool or type(temp)==int):
				if p[2] in env:
					print("Redeclaration Error")
				else:
					bool_dict[p[2]]=temp
					env[p[2]]=temp

			elif p[1]=="char"and type(temp)==str:
				if p[2] in env:
					print("Redeclaration Error")
				else:
					char_dict[p[2]]=temp
					env[p[2]]=temp

			else:
				print("Variable Type Error")
		elif p[0]=='var':
			if p[1]=='-':
				if p[2] not in env:
					print("undeclared variable")
				else:
					if p[2] in int_dict or p[2] in flt_dict:
						temp=env[p[2]]
						return -temp
					else:
						sys.exit("Type Error")
			else:
				if p[1] not in env:
					print("undeclared variable")
				else:
					return env[p[1]]
		elif p[0] == 'print_from_env':
			if p[1] in env:
				print(env[p[1]])
			else:
				sys.exit("Variable does not exist")

		elif p[0]=='print':
			if p[1]=='+':
				return str(run(p[2]))+" "+str(run(p[3]))
			else:
				# print(run(p[2]))
				list1=[]
				f_s=""
				list1=run(p[1])
				final_l=[]
				while (type(list1)==list):
					temp=list1[0]
					final_l.append(temp)
					list1=list1.pop()
				final_l.append(list1)
				xx=len(final_l)
				for x in range(xx):
					if x<xx-1:
						f_s=f_s + str(final_l[x])+" "
					else:
						f_s=f_s + str(final_l[x])
				print(f_s)
	else:
		return p

objLexer = lex.lex(module=Lexer)
objParser = yacc.yacc(module = Parser)
filename = sys.argv[-1]
filepath = "test_cases/" + filename
file1 = open(filepath, errors = 'ignore')
for lines in file1:
    objLexer.input(lines)
    parse_tree = objParser.parse(lines, lexer=objLexer)
    x = run(parse_tree)
    if x == None:
        continue
    else:
        print(x)