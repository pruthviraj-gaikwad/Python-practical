def roman(object,base=10):
	int_number = 0
	if(base in ['r','R']):
		for i in object:
			if i in ['I','V','X','L','C','D','M','i','v','x','l','c','d','m']:
				continue
			else:
				return "check object"
		return object

	if(type(object)==str):
		try :
			int_number=int(object,base)
		except ValueError:
			return "check object and base"

	if(type(object)==int or type(object)==float):
		int_number= int(object)
	dictionary ={1:"I",
                        5:"V",
                        10:"X",
                        50:"L",
                        100:"C",
                        500:"D",
                        1000:"M",
                        4:"IV",
                        9:"IX",
                       	40:"XL",
                       	90:"XC",
                        400:"CD",
                        900:"CM"
                    }
	if(int_number==0):
		return "zero has not roman representation"

	int_without_sign=int_number
	if(int_number<0):
		int_without_sign = -(int_number)
	s=""
	if int_without_sign in dictionary:
		if(int_number<0):
			return s+"-"+dictionary.get(int_without_sign)
		return s+dictionary.get(int_without_sign)
	else:
		l=[]
		for i in range(len(str(int(int_without_sign)))+1,1,-1):
			l.append(int_without_sign%(10**(i-1))-int_without_sign%(10**(i-2)))
		for i in range(len(l)):
			if l[i] in dictionary:
				s+=dictionary.get(l[i])
			else:
				j=0
				if(l[i]==0):
					continue
				elif(l[i]>1000):
					while(1000*j!=l[i]):
						s+=dictionary.get(1000)
						j+=1
					s+=dictionary.get(1000)	

				elif(l[i]>500 and l[i]<900):
					while(500+(100*j)!=l[i]):
						if(j==0):
							s+="D"
						else:
							s+=dictionary.get(100)
						j+=1
					s+=dictionary.get(100)

				elif(l[i]<500 and l[i]>100):
					while(100*j!=l[i]):
						s+="C"
						j+=1
					s+='C'

				elif(l[i]<100 and l[i]>50):
					while(50+10*j!=l[i]):
						if(j==0):
							s+="L"
						else:
							s+=dictionary.get(10)
						j+=1
					s+=dictionary.get(10)

				elif(l[i]>10 and l[i]<40):
					while(j*10!=l[i]):
						s+=dictionary.get(10)
						j+=1

				elif(l[i]<10 and l[i]>5):
					while(5+j*1!=l[i]):
						if(j==0):
							s+=dictionary.get(5)
						else:
							s+=dictionary.get(1)
						j+=1
					s+=dictionary.get(1)

				elif(l[i]<5 and l[i]>0):
					while(j*1!=l[i]):
						s+=dictionary.get(1)
						j+=1
				else:
					continue
	if int_number<0:
		return "-"+s
	return s

print(roman("0o0145",8))
print(roman(69))
print(roman("000123"))
print(roman("0x0A",16))
	
	
	
		