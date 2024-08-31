def slice(object,slicing_parameter):
	start_index=0
	last_index =0
	steps=1
	len_obj = len(object)
	if(type(object)==str):
		fun_call = result_text
	elif(type(object)==list):
		fun_call = result_list
	elif(type(object)==tuple):
		fun_call = result_tuple
	if(len(slicing_parameter)==0):
		start_index=0
		last_index=len_obj
		steps=1
		return fun_call(object,start_index,last_index,steps)

	elif(len(slicing_parameter)==1):
		steps=1
		last_index = len_obj
		if(slicing_parameter[0]==None):
			start_index=0	
			return fun_call(object,start_index,last_index,steps)
		else:
			if(slicing_parameter[0]<0):
				start_index = len_obj+ slicing_parameter[0]
				if(start_index<0):
					return ""
			if(slicing_parameter[0]>=0 and slicing_parameter[0]<len_obj):
				start_index = slicing_parameter[0]
			if(slicing_parameter[0]>=len_obj):
				return ""
		last_index=len_obj
		return fun_call(object,start_index,last_index,steps)

	elif(len(slicing_parameter)==2):
		steps=1
		if(slicing_parameter[0]==None):
			start_index=0
			if(slicing_parameter[1]==None):
				last_index = len_obj
				return fun_call(object,start_index,last_index,steps)	
		else:
			if(slicing_parameter[0]<0):
				start_index = len_obj+ slicing_parameter[0]
				if(start_index<0):
					return ""
			if(slicing_parameter[0]>=0 and slicing_parameter[0]<len_obj):
				start_index = slicing_parameter[0]
			if(slicing_parameter[0]>=len_obj):
				return ""
		if(slicing_parameter[1]==None):
			last_index=len_obj
		else:
			if(slicing_parameter[1]<0):
				last_index = len_obj+ slicing_parameter[1]
				if(start_index<0):
					return ""
			if(slicing_parameter[1]>=0 and slicing_parameter[1]<len_obj):
				last_index = slicing_parameter[1]
			if(slicing_parameter[1]>=len_obj):
				last_index = len_obj
		return fun_call(object,start_index,last_index,steps)

	else:
		if(slicing_parameter[2]==0):
			return " ValueError: slice step cannot be zero "
		if(slicing_parameter[2]==None):
			steps = 1
		else:
			steps = slicing_parameter[2]
		if(slicing_parameter[1]==None):
			last_index = 0 
			if(slicing_parameter[2]<0):
				last_index = -1
			if(slicing_parameter[2]>0):
				last_index = len_obj
		else:
			if(slicing_parameter[1]>len_obj):
				last_index = len_obj
			else:
				last_index = slicing_parameter[1]
			if(slicing_parameter[1]<0):
				last_index = len_obj+slicing_parameter[1]
		if(slicing_parameter[0]==None):
			start_index=0
			if(slicing_parameter[2]<0):
				start_index =len_obj-1
			slicing_parameter[0]=0
			if(start_index>=0 and last_index<start_index and steps<0):
					if(last_index<0):
						return fun_call(object,start_index,-1,steps)
					return fun_call(object,start_index,last_index,steps)
		else:
			start_index=slicing_parameter[0]
			if(slicing_parameter[0]<=0 and slicing_parameter[1]<0 and slicing_parameter[2]<0):
				start_index = slicing_parameter[0]+len_obj
				if(slicing_parameter[0]== slicing_parameter[1]):
					return ""
				if(slicing_parameter[0]==0 and last_index<0):
					return fun_call(object,0,-1,steps)
				if(start_index<last_index and last_index<0 and start_index<0):
					return ""
				if(start_index>last_index and last_index<0 and start_index<0):
					return ""
				if(start_index>last_index and last_index<0 and start_index>=0):
					return fun_call(object,start_index,-1,steps)
				if(start_index>last_index and last_index<len_obj and start_index>=0):
					return fun_call(object,start_index,last_index,steps)
				if(start_index<last_index):
					return ""
				if(start_index==0):
					return ""
			else:
				if(start_index<0):
					start_index = len_obj + slicing_parameter[0]
					return fun_call(object,start_index,last_index,steps)
				elif(start_index>=0 and last_index<start_index and steps<0):
					if(last_index<0):
						return fun_call(object,start_index,-1,steps)
					return fun_call(object,start_index,last_index,steps)
	return fun_call(object,start_index,last_index,steps)
				
def result_text(object,start_index,last_index,steps):
	text=""
	for i in range(start_index,last_index,steps):
		text+=object[i]
	return text
	
def result_list(object,start_index,last_index,steps):
	list_result=[]
	for i in range(start_index,last_index,steps):
		list_result+=[object[i]]
	return list_result

def result_tuple(object,start_index,last_index,steps):
	tuple_result=()
	for i in range(start_index,last_index,steps):
		tuple_result+=tuple([object[i]])
	return tuple_result

print(slice("pruthvi",[-1,8,1]))
print(slice("prem",[2,2]))
print(slice([2,3,4,5,3],[9,9]))
