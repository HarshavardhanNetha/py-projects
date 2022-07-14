("write a programme to caluculate roots of a quadratic equation")
a=int(input("enter coefficient of X^2:"))
b=int(input("enter coefficient of X:"))
c=int(input("enter coefficient of constant:"))
d=b**2-4*a*c
if(d>0):
	print("rooots are real and distant")
	print("rooots are ="(-b+d**0.5)/(2*a),(-b-d**0.5)/(2*a))
elif(d==0):
	print("roots are real and equal")
	print("roots are=",-b/2*a,-b/2*a)
else:
	print("roots are imaginary")
