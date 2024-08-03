def print_pat(len):
	for i in range(len):
		for j in range(len):
			print("*",end="")
		print("")

def print_pate(len):
	for i in range(0,(len//2)+1):
		for j in range(0,len):
			if j==(len//2)-i:
				print("*",end="")
			elif i==j==(len//2):
				print(len,end="")
			elif j==(len//2)+i:
				print("*",end="")	
			else:
				print(" ",end="")
		print("")
		
	for i in range(0,(len//2)):
		for j in range(0,len):
			if j==i+1:
				print("*",end="")
			elif j==(len-1)-i-1:
				print("*",end="")
				break	
			else:
				print(" ",end="")
			
		print("")
#main program-->
def print_pattern(len):
	if(len<1):
		return "enter len greater than 1 or equal to 1"
	w =str(len)
	i = 0
	q=w.split(".")
	i=int(len)
	if(w.isdigit()):
		return print_p(i)
	if(q[0].isdigit()==True and q[1]>"0"):
		return "enter positive value"
	else:
                return print_p(i)

	return print_p(i)
	
def print_p(len):
	column = ((len*2)+3)
	kite = ((len*2)+1)
	lst_row = len
	for i in range(0,(kite//2)):
		for j in range(0,kite+2):
			if j==(kite//2)-i+1:
				print("*",end="")
			elif j==(kite//2)+i+1:
				print("*",end="")
			else:
				print(" ",end="")
			
		print("")
	
	for i in range(1):
		for j in range(0,kite+2):
			if (j==i+1):
				print("*",end="")
			elif j==((kite+2)//2):
				print(len,end="")
			elif j==kite:
				print("*",end="")
				break
			else:
				print(" ",end="")
		print("")
		
	for i in range(0,(kite//2)-1):
		for j in range(0,kite+1):
			if j==i+2:
				print("*",end="")
			elif j==(kite+1)-i-2:
				print("*",end="")	
			else:
				print(" ",end="")
			
		print("")
		
	for i in range(0,lst_row):
		for j in range(0,column):
			print("*",end="")
		print("")
	return ""

for i in range(6):
	print(print_pattern(i))

print(print_pattern(1))
