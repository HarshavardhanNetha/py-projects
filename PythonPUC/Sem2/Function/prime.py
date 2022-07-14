a=int(input())
ant=0
for i in range(2,(a//2)+1):
    if(a%i==0):
        ant=1
        break
if(ant==0):
        print('Prime Number')
else:
        print('Not Prime')
