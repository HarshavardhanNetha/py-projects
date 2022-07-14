a="1"
aa="Veg Manchuria"
b="2"
bb="Egg Rice"
c="3"
cc="Kasata"
d="4"
dd="Noodles"
e="5"
ee="Coke"
a1=int(40)
b1=int(50)
c1=int(30)
d1=int(35)
e1=int(20)
n=1
while(n>0):
	temp=int(input("Order Id:"))
	while(temp>0):
		if(temp==1):
			q1=int(input("Quantity:"))
			print("Order Name:",aa)
			print("Value =",a1*q1)
		else:
			if(temp==2):
				q2=int(input("Quantity:"))
				print("Order Name:",bb)
				print("Value =",b1*q2)
			else:
				if(temp==3):
					q3=int(input("Quantity:"))
					print("Order Name:",cc)
					print("Value =",c1*q3)
		'''if(temp==4):
			q4=int(input("Quantity:"))
			print("Order Name:",dd)
			print("Value =",d1*q4)
		if(temp==5):
			q5=int(input("Quantity:"))
			print("Order Name:",ee)
			print("Value =",e1*q5)'''
		temp=0
	n=0
