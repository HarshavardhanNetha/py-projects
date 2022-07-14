n=int(input("Any Number"))
p=n
rev=0
while(n>0):
	rem=n%10
	rev=rev*10+rem
	n=n//10
if(rev==p):
	print("The NUmber is Polindrome...!!")
else:
	print("Not a polindrome..!")	
