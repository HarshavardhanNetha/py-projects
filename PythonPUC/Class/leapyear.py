#leap year or not
a=int(input("Year:"))
if(a%4==0 and a%100!=0)or(a%400==0):
	print("Leap Year")
else:
	print("Not Leap Year")

'''if(a%400==0):
	print(a,"is leap year")
elif(a%4==0):
	if(a%100==0):
		print(a,"is leap year")2**7
	else:
		print(a,"is not leap year")
else:
	print(a,"is not leap year")'''
