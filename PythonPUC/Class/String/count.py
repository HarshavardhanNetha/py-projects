#wap to count the no. of occurances of each word in given sentence/string
a=input()
l=a.split()
print(l)
no_dup=[]
for i in l:
    if i not in no_dup:
        no_dup.append(i)
        c=l.count(i)
        print(c)
#on hold.......
