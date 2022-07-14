l=[]
for i in range(101):
    l.append(i)
def per_num(l):
    list=[]
    sum=0
    for i in l:
        for j in range(1,100):
            if(i%j==0):
                sum+=i
        if(sum==l):
            list.append(sum)
    print(list)
