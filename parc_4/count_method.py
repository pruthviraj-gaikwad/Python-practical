def count(original_string,maching_string,b):
	c =0
	a =[]
	bool=False
	if(maching_string==''):
		for i in range(len(original_string)):
			if(original_string[0]==''):
				bool=True 
				c+=1
			else:
				continue
		if(bool==True):
			return c
		else:
			return len(original_string)+1
			
	if maching_string==original_string:
		return 1

	if(b==True):
		for i in range(len(original_string)):
			for j in range(len(original_string)):
				a.append(original_string[i:j+1])

		for i in range(len(a)):
			if(a[i]==maching_string):
				c+=1
	else:
		s1=''
		d =0
		c =0
		for i in range(len(original_string)-len(maching_string)):
			s1=''
			if(original_string[i]==s[0]):
				for j in range(i,i+len(maching_string)):
					s1+=original_string[j]
			if maching_string==s1:
				c+=1
				i = j+1
			else:
				continue

	return c
	

print(count("sgsggsgggg","gg",False))
