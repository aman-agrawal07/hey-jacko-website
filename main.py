from datetime import datetime

def remove_leading_zeros(value):
		value		=	str(value)
		if(value[0]=='0'):
			value	=	value[1:]
		return int(value)
	
	
def solution(S):
	# write your code in Python 3.6
	phone_numbers	=	{}
	phone_consume	=	{}
	checking			=	[]
	logs_lines		=	S.split("\n")
	for eachlog in logs_lines:
		time_num			=	eachlog.split(',')
		
		if(phone_numbers.get( time_num[1] ) is None):
			time_log		=	time_num[0].split(':')
			phone_numbers[time_num[1]]	=	[remove_leading_zeros(time_log[0]),remove_leading_zeros(time_log[1]),remove_leading_zeros(time_log[2]) ]
		else:
			time_log		=	time_num[0].split(':')
			hh					=	remove_leading_zeros(time_log[0])
			mm					=	remove_leading_zeros(time_log[1])
			ss					=	remove_leading_zeros(time_log[2])
			
			hh_old			=	phone_numbers[time_num[1]][0]
			mm_old			=	phone_numbers[time_num[1]][1]
			ss_old			=	phone_numbers[time_num[1]][2]
			
			phone_numbers[time_num[1]]	=	[hh+hh_old, mm+mm_old, ss+ss_old ]
	
	for ph,tm in phone_numbers.items():
		consume				=	(tm[0]*3600)+(tm[1]*60)+tm[2]
		phone_consume[int(ph.replace('-',''))]	=	[consume,ph,tm]
		
	for ph,tm in phone_consume.items():
		checking.append(tm[0])
	
	max_call				=	max(checking)
	
	for ph,tm in phone_consume.items():
		if(tm[0]==max_call):
			deletion=ph
			del phone_numbers[tm[1]]
	
	del phone_consume[deletion]
	print(phone_consume)
	# bill=0
	# for ph,tm in phone_numbers.items():
		
    
    
solution("00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090")
# print(remove_leading_zeros('24'))

