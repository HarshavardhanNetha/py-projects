#inheritence
class A:
    def sayHello(a):
        print('Hello World!')
class B:
    def sayHi(a):
        print('Hii')
class C(A,B):
    def sayNo(a):
        print('Noo.....!!')

a=C()
a.sayHi()
a.sayHello()
a.sayNo()
