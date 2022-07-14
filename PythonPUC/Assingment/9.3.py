import random
a=random.randint(1,101)
cnt=0
while(1):
    b=int(input())
    cnt+=1
    if(b==a):
        print('Congo...! You guessed it right in %d guesses.'%(cnt))
        break
    elif(b<a):
        print('Your guess is too low')
    else:
        print('Your guess is too high')
