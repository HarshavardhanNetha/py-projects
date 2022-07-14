l=[]
n=int(input('Length of the list:'))
for i in range(1,n+1):
    k=int(input('Enter the number:'))
    l.append(k)
def sum_list(l):
    if(len(l)==1):
        return l[0]
    else:
        return l[0]+sum_list(l[1:])
print(sum_list(l))
