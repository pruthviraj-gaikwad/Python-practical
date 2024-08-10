def count(ms,s,b):
	c =0
	a =[]
	if(s==''):
		return 
	if s==ms:
		return 1
	if(b==True):
		for i in range(len(ms)):
			for j in range(len(ms)):
				a.append(ms[i:j+1])

		for i in range(len(a)):
			if(a[i]==s):
				c+=1
	else:
		s1=''
		d =0
		c =0
		for i in range(len(ms)-len(s)):
			s1=''
			i=d
			if(ms[i]==s[0]):
				for j in range(i,i+len(s)):
					s1+=ms[j]
			if s==s1:
				c+=1
				d = j+1
			else:
				d = i+1
				continue

	return c
	

print(count("sgsggsgggg","gg",False))