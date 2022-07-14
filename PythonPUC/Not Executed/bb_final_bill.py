aa="Veg Manchuria"
bb="Egg Rice"
cc="Kasata"
dd="Noodles"
ee="Coke"
a1=int(40)
b1=int(50)
c1=int(30)
d1=int(35)
e1=int(20)
n=1
while(n!=0):
	if(True):
		q1=int(input("Quantity of Veg Manchuria:"))
	if(True):
		q2=int(input("Quantity of Egg Rice:"))
	if(True):
		q3=int(input("Quantity of Kasata:"))
	if(True):
		q4=int(input("Quantity of Noodles:"))
	if(True):
		q5=int(input("Quantity of Coke:"))
	n=0
print("----------------------------------------")
if(q1!=0):
	print("Order Name:",aa,"\tValue =",a1*q1)
if(q2!=0):
	print("Order Name:",bb,"\t\tValue =",b1*q2)
if(q3!=0):
	print("Order Name:",cc,"\t\tValue =",c1*q3)
if(q4!=0):
	print("Order Name:",dd,"\t\tValue =",d1*q4)
if(q5!=0):
	print("Order Name:",ee,"\t\tValue =",e1*q5)
print("-----------------------------------------")
print("Total amnt to be paid is",a1*q1+b1*q2+c1*q3+(d1*q4)+(e1*q5))
print("----------THANK_YOU-VISIT_AGAIN----------")
