d1={'Sharan':[15,12,13,10,9,8],'Akhil Reddy':[15,14,13,14,9,9],'Kiran':[13,14,15,14,13,14]}
d2={}
for i,val in d1.items():
    s=sum(val)
    d2[i]=s
print(d1)
print(d2)
for i,j in d2.items():
    if(j==max(d2.values())):
        print(i,"is topper")
