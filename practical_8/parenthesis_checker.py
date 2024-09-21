def check_string(exp):
	valid_list = ["(","{","[","<",")","}","]",">","a", "b", "c"," d", "e", "f", "g", "h"," i", "j", "k"," l", "m", "n", "o", "p", "q", "r", "s", "t", "u"," v", "w", "x", "y"," z",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', ' V', 'W', 'X', 'Y', 'Z',"*","^","+","-",'/']
	valid_string = False
	for latter in exp:
		if(latter in valid_list):
			valid_string = True
		else:
			return False
	return valid_string

def count_valid_par(exp):
	valid=0
	unvalid=0
	for string in exp:
		if(type(string)==str and check_string(string)):
			if(valid_parenthesis(string)):
				valid+=1
			else:
				unvalid+=1
		elif(type(string)==str and check_string(string)==False):
			unvalid+=1
		elif(type(string)==list or type(string)==tuple):
			valid+=count_valid_par(string)[0]
			unvalid+=count_valid_par(string)[1]
		elif(type(string)==set):
			string = list(string)
			valid+=count_valid_par(string)[0]
			unvalid+=count_valid_par(string)[1]
		elif(type(string)==int or type(string)==float):
			unvalid+=1
	return [valid,unvalid]
			

def valid_parenthesis(exp):
	if(check_string(exp)==False):
		return False
	open_bracket="({[<"
	close_bracket=")}]>"
	list1=[]
	dict1={
		"(":")",
		"{":"}",
		"[":"]",
		"<":">"
	}
		
	if len(exp)==1:
		return False
	for latter in exp:
		if(latter in open_bracket):
			list1.append(latter)
		elif(latter in close_bracket):
			if(list1==[]):
				return False
			else:
				char = list1.pop()
				if(dict1[char]==latter):
					continue
				else:
					return False
	if(list1==[]):
		return True
	else:
		return False

print(count_valid_par([1,2,"()",set([2,2,"()",")",
'(','{}']),tuple([3,4,"()"])])) 
print(count_valid_par([1,2,"3kdsk","(){}<>{}","()",set([2,2,"()",")",
'(','{}']),tuple([3,4,"()"])]))




