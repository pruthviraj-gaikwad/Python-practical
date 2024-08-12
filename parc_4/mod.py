def modd(n,d):
	q = n//d
	reminder =q*d
	return n-reminder
print(modd(5,3))
print(modd(2,1))
print(modd(1,1))
#print(modd(0,0))->zero division error
