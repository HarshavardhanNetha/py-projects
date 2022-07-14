#wap to add an ing at the end of the string if already  its ing replace with ly else add ing
a=input()
if(len(a)<3):
    print(a+'ing')
elif(a[-3:]=='ing'):
    print(a+'ly')
else:
    print(a+'ing')
