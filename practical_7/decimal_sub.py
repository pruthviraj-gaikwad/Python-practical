def decimal_substraction(num1,num2):
	with_sign_num1 = str_to_int(num1)
	with_sign_num2 = str_to_int(num2)
	num1_list=[]
	num2_list=[]
	if(with_sign_num1<with_sign_num2):
		with_sign_num1,with_sign_num2 = with_sign_num2,with_sign_num1
		num1_list.extend(num2)
		num2_list.extend(num1)
	else:
		num1_list.extend(num1)
		num2_list.extend(num2)
	if(len(num1_list)!=len(num2_list)):
		k = len(num1_list)-len(num2_list)
		for i in range(k):
			num2_list.insert(i,'0')
	i=len(num1_list)-1
	j=len(num2_list)-1
	result_string = ''
	n1 = 0
	n2 = 0
	n  = 0
	while(j!=-1):
		n1= str_to_int(num1_list[i])
		n2 = str_to_int(num2_list[j])
		if(n2>n1):
			if(num1_list[j-1]=='0'):
				for k in range(j-1,-len(num1_list)-1,-1):
					if(num1_list[k]=='0'):
						num1_list[k]='9'
					if(str_to_int(num1_list[k])>0):
						n = str_to_int(num1_list[j-1])-1
						num1_list[k]=str(n)
						break
				result_string=str(n1-n2)+result_string
			else:
				n = str_to_int(num1_list[j-1])-1
				num1_list[j-1]=str(n)
				n1+=10
				result_string=str(n1-n2)+result_string
			j-=1
			i-=1
				
		else:
			result_string=str(n1-n2)+result_string
			j-=1
			i-=1
	if(str_to_int(num1)<str_to_int(num2)):
		return -str_to_int(result_string)
	else:
		return str_to_int(result_string)
			
dictionary_of_number={'0':0,
				'1':1,
				'2':2,
				'3':3,
				'4':4,
				'5':5,
				'6':6,
				'7':7,
				'8':8,
				'9':9}
def str_to_int(text):
	if(len(text)==0):
		return 0
	if(len(text)==1):
		return dictionary_of_number[text]
	else:
	
		actual_number=0
		if(text.isdigit()):
			k=len(text)-1
			for i in text:
				actual_number+=dictionary_of_number.get(i)*(10**k)
				k-=1
			
			return actual_number

print(decimal_substraction("13","2"))