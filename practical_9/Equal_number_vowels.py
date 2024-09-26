vowels = "AEIOUaeiou"

def count_vowels(L):
	count = 0
	for latter in L:
		if type(latter) in [list,tuple,set]:
			count+=count_vowels(list(latter))
		elif type(latter)==str:
			count+=is_equal_vowels(latter)
	return count

def is_equal_vowels(latter):
	vowels_dict={}
	for symbol in latter:
		if (symbol in vowels):
			if(symbol in vowels_dict):
				vowels_dict[symbol]+=1
			else:
				vowels_dict.setdefault(symbol,1)

	return len(vowels_dict)*(list(vowels_dict.values())[0])==sum(vowels_dict.values())


print(count_vowels(["aeiouhfhskaeiou","aeAi"]))
	
			