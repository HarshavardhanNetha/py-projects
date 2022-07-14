input("salary")
gender=input("enter gender:")
salary=int("enter the salary:")
if(salary<10000):
	if (gender=="male"):
		print("salary of male=",salary+(salary*8)/100
	else :
		print("salary of female=",salary+(salary*13)/100)
else:
	if(gender=="male"):
		print("salary of male=",salary+(salary*5)/100)
	else:
		print("salary of female=",salary+(salary*10)/100)
