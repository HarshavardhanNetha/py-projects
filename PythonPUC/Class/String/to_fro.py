#wap
s=input()
if(len(s)<=2):
    print(s)
else:
    s2=s[0:2]+s[-2:]
    print(s2)
