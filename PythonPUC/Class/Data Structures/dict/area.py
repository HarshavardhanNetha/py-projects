#wap to print dic with radius of circle as key & its area as value until you enter -1
d={}
while(1):
    a=int(input())
    if(a==-1):
        break
    else:
        d[a]=round(3.14*a*a)
print(d)
