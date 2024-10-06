import time

obj =[list,tuple,set]
 
def count_palindrome(L):
	count=0

	for latter in L:
		if type(latter) in obj:
			count+=count_palindrome(list(latter))
		else:
			if(type(latter)==int):
				latter = str(latter)
		
		count+=(type(latter)==str and len(latter)%6==3 and latter==latter[::-1])
	return count

def count_pal_me(L):
	count=0
	for latter in L:
		if type(latter)==str:
			if(len(latter)%6==3):
				if(latter==latter[::-1]):
					count+=1
		elif type(latter) == int:
			latter = str(latter)
			if(len(latter)%6==3):
				if latter == latter[::-1]:
					count+=1
		elif type(latter) in obj:
			count+=count_pal_me(list(latter))

	return count


def check_performance(approches):
	time_list = []
	for approch in approches:
		temp_list=[]
		for i in range(500000):
			start_time=time.time()
			approch([111,121,3,4,set([1,2,"sss","ppp"]),(2,"ggggggggg",121,999),123444321,"ppppppppp","###","pruthvi",{121,888,999}])
			end_time=time.time()
			temp_list.append(end_time-start_time)
		time_list.append((sum(temp_list)/500000))
	return time_list

def which_better(approche):
	if(approche[0]>approche[1]):
		return "peformance incresed by %d"%((abs(approche[0]-approche[1])*100)/approche[0])
	else:
		return "performance decrease by %d"%((abs(approche[0]-approche[1])*100)/approche[1])

print(check_performance([count_pal_me,count_palindrome]))
print(which_better(check_performance([count_pal_me,count_palindrome])))











	