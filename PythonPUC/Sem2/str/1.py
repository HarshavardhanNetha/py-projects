a=input()
x=[]
for i in a:
  if(i not in x):
    x.append(i)
    print(i,a.count(i),end='  ')
