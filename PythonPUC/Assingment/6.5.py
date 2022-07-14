a='any string to g=find 782648672  in vowels consonants whitespaces 873'
v=c=d=w=0
print(len(a))
for i in a:
    if(i in list('AEIOUaeiou')):
        v+=1
    elif(i.isdigit()):
        d+=1
    elif(i==" "):
        w+=1
    else:
        c+=1
print(' Vowels are {} \n Consonants are {} \n Digits are {} \n Whitespaces are {}'.format(v,c,d,w))
print(v+d+w+c)
