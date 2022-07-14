n=int(input("Enter number::"))
rev=0
rem=0
while(n>0):
	rem=n%10
	rev=rev*10+rem
	n=n//10
print(rev)
#the reason for not executing the prgm bfr is we used n/10, sol:FLOOR DIVISION


