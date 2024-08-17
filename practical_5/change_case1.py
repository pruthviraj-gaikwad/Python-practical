def change_case(text,style):
	result_text=""
	ord_result=0
	if style in ["c",'C']:
		return capital_case(text)
	elif style in ['s','S']:
		return small_case(text)
	elif style in ['r','R']:
		return reverse_case(text)
	elif style in ['z','Z']:
		return zic_zac_case(text)

def capital_case(text):
	result_text=""
	ord_result=0
	for char in text:
		if(int(ord(char))>=65 and int(ord(char))<=90):
			result_text+=""+char
		else:
			ord_result = ord(char)-32
			result_text+=chr(ord_result)
	return result_text

def small_case(text):
	result_text=""
	ord_result=0
	for char in text:
		if(int(ord(char))>=97 and int(ord(char))<=122):
			result_text+=char
		else:
			ord_result = ord(char)+32
			result_text+=chr(ord_result)
	return result_text

def reverse_case(text):
	result_text=""
	ord_result=0
	for char in text:
		if(int(ord(char))>=65 and int(ord(char))<=90):
			ord_result = ord(char)+32
			result_text+=chr(ord_result)
		else:
			ord_result = ord(char)-32
			result_text+=chr(ord_result)
	return result_text
	
def zic_zac_case(text):
	result_text=""
	ord_result=0
	if(int(ord(text[0]))>=65 and int(ord(text[0]))<=90):
		result_text+=text[0]
		for i in range(1,len(text)):
			if(i%2==0):
				if(int(ord(text[i]))>=65 and int(ord(text[i]))<=90):
					result_text+=""+text[i]
				else:
					ord_result = ord(text[i])-32
					result_text+=chr(ord_result)
			else:
				if(int(ord(text[i]))>=97 and int(ord(text[i]))<=122):
					result_text+=text[i]
				else:
					ord_result = ord(text[i])+32
					result_text+=chr(ord_result)
	else:
		result_text+=text[0]
		for i in range(1,len(text)):
			if(i%2!=0):
				if(int(ord(text[i]))>=65 and int(ord(text[i]))<=90):
					result_text+=""+text[i]
				else:
					ord_result = ord(text[i])-32
					result_text+=chr(ord_result)
			else:
				if(int(ord(text[i]))>=97 and int(ord(text[i]))<=122):
					result_text+=text[i]
				else:
					ord_result = ord(text[i])+32
					result_text+=chr(ord_result)
	return result_text

print(change_case("sggs","c"))
print(change_case("SgGs","S"))
print(change_case("SgGs",'r'))
print(change_case("Sggs",'z'))
print(change_case("sGGs","Z"))


				
				
			