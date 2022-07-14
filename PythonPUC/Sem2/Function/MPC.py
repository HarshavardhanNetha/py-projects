#read marks of MPC write a function to calculate total marks with user inputs and avg also with previous function
def MPC(a,b,c):
    return (a+b+c)
a=int(input())
b=int(input())
c=int(input())
x=MPC(a,b,c)
print('Total Marks:',x)
def avg(a):
    print('Average:',a/3)
avg(x)
