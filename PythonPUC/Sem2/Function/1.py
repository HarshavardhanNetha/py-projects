def sayhello():
    print('Holla')
sayhello() #function without arguments


def sum(a,b):
    print(a+b) 
sum(5,9) #function with arguments


def add2(a,b):
    return a+b
print(add2(73,4))
add2(54,53) #wont print cause return value will print only when we use print()


def sayName(a):
    print('Hello')
    return a
name=sayName('Harsha')
sayName('Ram')
print(sayName('Ram'))
print(name) #prints only the value which is returned in any function


class Harsha:
    def sum3(a,b):
        print(a+b)
    def multiply(a,b):
        print(a*b)
    def divide(a,b):
        print(a//b)
z=Harsha
z.sum3(4,5)
z.multiply(5,8)
z.divide(100,20)
