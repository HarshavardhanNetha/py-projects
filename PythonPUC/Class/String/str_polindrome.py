#string operations
#WAP to check whether a given string is polindrome or not
a=input('Enter a string:')
b=a[::-1]
if(a==b):
    print('Polindrome')
else:
    print('Not a polindrome')

#other way
le=len(a)-1
while(le>=0):
    print(a[le],end='')
    le-=1
