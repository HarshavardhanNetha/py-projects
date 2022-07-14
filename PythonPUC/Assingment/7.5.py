def hyp(a,b):
    x=a*a+b*b
    print('Hypotenuse is {}'.format(round(x**0.5,2)))
a=int(input('adj side:'))
b=int(input('opp side:'))
hyp(a,b)
