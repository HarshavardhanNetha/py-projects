l=[]
for i in range(6):
    a=input()
    try:
        x=int(a)
    except:
        l.append(a)
print(l)
