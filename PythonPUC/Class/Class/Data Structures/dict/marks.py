d={'Harsha':(12,13,14,15,14),'Ravi':(13,14,14,15,15,14),'Srikanth':(15,14,15,15,14,14)}
d2={}
for i,j in d.items():
    sum1=sum(j)
    d2[i]=sum1
print(d)
print(d2)
for k in d2.values():
    print()
