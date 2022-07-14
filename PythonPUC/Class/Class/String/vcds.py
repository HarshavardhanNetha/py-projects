#wap to count the no of vowels,consonents,digits and spaces
s1=input()
v=c=d=s=0
for i in s1:
    if(i in list('aeiouAEIOU')):
        v+=1
    elif(i.isdigit()):
        d+=1
    elif(i.isspace()):
        s+=1
    else:
        c+=1
print('Vowels={} Consonants={} Digits={} Spaces={}'.format(v,c,d,s))
