def change_case(text,style):
	result_text=""
	ord_result=0
	if(style=="c" or style=="C"):
		for i in range(len(text)):
			if(int(ord(text[i]))>=65 and int(ord(text[i]))<=90):
				result_text+=""+text[i]
			else:
				ord_result = ord(text[i])-97+65
				result_text+=chr(ord_result)
		return result_text
	elif(style=="S" or style=="s"):
		for i in range(len(text)):
			if(int(ord(text[i]))>=97 and int(ord(text[i]))<=122):
				result_text+=text[i]
			else:
				ord_result = ord(text[i])-65+97
				result_text+=chr(ord_result)
		return result_text
	elif(style=="R" or style=="r"):
		for i in range(len(text)):
			if(int(ord(text[i]))>=65 and int(ord(text[i]))<=90):
				ord_result = ord(text[i])-65+97
				result_text+=chr(ord_result)
			else:
				ord_result = ord(text[i])-97+65
				result_text+=chr(ord_result)
		return result_text
	elif(style=="Z" or style=='z'):
		if(int(ord(text[0]))>=65 and int(ord(text[0]))<=90):
			result_text+=text[0]
			for i in range(1,len(text)):
				if(i%2==0):
					if(int(ord(text[i]))>=65 and int(ord(text[i]))<=90):
						result_text+=""+text[i]
					else:
						ord_result = ord(text[i])-97+65
						result_text+=chr(ord_result)
				else:
					if(int(ord(text[i]))>=97 and int(ord(text[i]))<=122):
						result_text+=text[i]
					else:
						ord_result = ord(text[i])-65+97
						result_text+=chr(ord_result)
		else:
			result_text+=text[0]
			for i in range(1,len(text)):
				if(i%2!=0):
					if(int(ord(text[i]))>=65 and int(ord(text[i]))<=90):
						result_text+=""+text[i]
					else:
						ord_result = ord(text[i])-97+65
						result_text+=chr(ord_result)
				else:
					if(int(ord(text[i]))>=97 and int(ord(text[i]))<=122):
						result_text+=text[i]
					else:
						ord_result = ord(text[i])-65+97
						result_text+=chr(ord_result)
		return result_text


print(change_case("sggs","c"))
print(change_case("SgGs","S"))
print(change_case("SgGs",'r'))
print(change_case("Sggs",'z'))
print(change_case("sGGs","Z"))


				
				
			