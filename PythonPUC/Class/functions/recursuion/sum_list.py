l=[1,2,3,4,5,66]
def sum_list(l):
    if(len(l)==1):
        return l[0]
    else:
        return l[0]+sum_list(l[1:])
print(sum_list(l))
