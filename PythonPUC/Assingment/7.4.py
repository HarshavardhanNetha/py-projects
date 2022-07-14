print('Welcome to demo of user and pre defined functions.')
a=int(input('Which example would you like to read first..? \n Press 1 for Pre defined function \n Press 2 for user defined function'))
def pre():
    print('*Pre Defined functions*')
    print('These are the functions which are already written inbuilt \n Ex. str.isspace(),str.isupper(),sorted(dict) etc')
def usr():
    print('*User Defined functions*')
    print('They can be created by user \n Syntax: def function_name(arguments) \n \t statement 1 \n \t statement 2 \n \t ..........')
print()
print()
if(a==1):
    pre()
    print()
    usr()
else:
    usr()
    print()
    pre()
