l=[]
obj = [list,set,tuple]
def get_ss_sl(L):
	for num in L:
		if type(num)==int:
			l.append(num)
		elif type(num) in obj:
			get_ss_sl(num)
		elif type(num)==dict:
			get_ss_sl(list(num.values()))

get_ss_sl([1,2,3,4,5,6,[1,1,3,4],{2,3,5,90},{1:20,32:300},(5,3,5,1000)])
l.sort()
num=l

for i in range(len(l)-1):
	if(num[i]==num[i+1]):
		continue
	else:
		print(num[i+1])
		break

for i in range(len(l)-1,-len(l)-1,-1):
	if(num[i]==num[i-1]):
		continue
	else:
		print(num[i-1])
		break
		
l.clear()