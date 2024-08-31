alpha ={'a','b'}
final_state = {'q1'}

def q0(text):
	if len(text)>0 :
		symbol = text[0]
		if symbol in ['a','b']:
			if symbol == "a":
				return q0(text[1:])
			else:
				return q1(text[1:])
		else:
			return -1
	return "q0"
	
def q1(text):
	if(len(text)>0):
		symbol = text[0]
		if symbol in ['a','b']:
			if symbol == "a":
				return q0(text[1:])
			else:
				return q1(text[1:])
		else:
			return -1
	return "q1"

def dfa(text):
	return q0(text)

text = "abbababab"

if dfa(text) in final_state :
	print(" Accepted ")
else:
	print(" Rejected ")



