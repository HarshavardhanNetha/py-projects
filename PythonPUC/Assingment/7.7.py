def amnt(a):
    amnt=0
    x=int(input('Amount:'))
    if(a>60):
        amnt=0.1*x+x
    else:
        amnt=0.12*x+x
    print(amnt)
t=int(input('Age..?'))
amnt(t)
