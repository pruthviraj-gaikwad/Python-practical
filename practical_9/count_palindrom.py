obj =[list,tuple,set]
 
def count_palindrome(L):
	count=0

	for latter in L:
		if type(latter) in obj:
			count+=count_palindrome(list(latter))
		else:
			if(type(latter)==int):
				latter = str(latter)
		
		count+=(type(latter)==str and len(latter)%6==3 and is_palindrome(latter))
	return count

def is_palindrome(string):
	return string==string[::-1]

print(count_palindrome(["aaa","bbb","bbbbb",[111,"aaa",121]]))
		
				