#write a python function to check whether the given string is polindrome or not
def poly(a):
    b=a[-1::-1]
    if(a==b):
        print( 'Polindrome'  )
    else:
        print('Not a Polindrom')
#other way
def pol(a):
    l=0
    r=len(a)-1
    while(l<=r):
        if(not a[l]==a[r]):
            print( False )
        l+=1
        r-=1
    print(True)

a=input()
poly(a)
pol(a)


        
def po(a):
    b=''
    l=len(a)-1
    while(l>=0):
        b=b+a[l]
        l-=1
    if(a==b):
        print( 'Polindrome'  )
    else:
        print('Not a Polindrom')
po(a)
