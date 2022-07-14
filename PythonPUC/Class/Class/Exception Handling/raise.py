#raising error
l=int(input())
try:
    if(l<10):
        raise KeyError('Enter number less than 10')
except KeyError as myown:
    print(myown)
    
