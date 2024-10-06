def get_even_odd_count(L):
	even_sum,odd_sum=0,0
	for num in L:
		if(num%2==0):
			even_sum+=1
		else:
			odd_sum+=1

	return [even_sum,odd_sum]

def f1(L):
	even_sum,odd_sum=0,0
	for num in L:
		if num%2:
			odd_sum+=1
		else:
			even_sum+=1

	return [even_sum,odd_sum]

def f2(L):
	even_sum,odd_sum=0,0
	for num in L:
		odd_sum+=(num%2)
		even_sum+=1-(num%2)

	return [even_sum,odd_sum]

def f3(L):
	even_sum,odd_sum=0,0
	for num in L:
		odd_sum+=(num&1)
		even_sum+=1-(num&1)

	return [even_sum,odd_sum]


def get_even(L):
	even_sum=0
	if(len(L)==0):
		return 0
	return (L[0]%2==0)+get_even(L[1:])

print(get_even_odd_count([2,3,4,10,11,2,4,3,9]))
print(get_even([2,3,4,10,11,2,4,3,9]))
print(f1([2,3,4,10,11,2,4,3,9]))
print(f2([2,3,4,10,11,2,4,3,9]))
print(f3([2,3,4,10,11,2,4,3,9]))