n=int(input("Number::"))
p=n
rev=0
while(n>0):
	rem=n%10
	rev=rev+(rem*rem*rem)
	n//=10
if(rev==p):
	print("Armstrong..!")
else:
	print("Not Armstrong..!!")
