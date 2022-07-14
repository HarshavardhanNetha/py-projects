a=int(input("Number:"))
n=2
cnt=0
while(n<a):
	if(a%n==0):
		cnt+=1
	n+=1
if(cnt==0):
	print("Prime")
else:
	print("Not Prime")
