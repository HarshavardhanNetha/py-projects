#inheritence
class A:
    def sayHello(a):
        print('Hello World!')
class B(A):
    def sayHi(a):
        print('Hii')
class C(A):
    def sayNo(a):
        print('Noo.....!!')

a=B()
a.sayHi()
a.sayHello()
#a.sayNo()
