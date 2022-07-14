#class name marks, functions stuname stumarks,printmarks
#stu marks nd name function shld have 1 prameter as list
#prnt marks shl dhave 1 parameter in strng
#stu marks will print markls of all students , stu name shld print names of all students ,
#print marks function shd print marks of given student name or student not found if student name is not available
#read student names and marlks from ythe user with user defined inputs and size
#size shld be equal to the both list
#read stu name frm user to prnt marks
l1=[]
l2=[]
s=int(input('Size of list:'))
for i in range(s):
    x=input('Name:')
    l1.append(x)
    y=int(input('Marks'))
    l2.append(y)
class clas:
    def name(a,l1):
        for i in l1:
            print(i,end=' ')
    def marks(a,l2):
        for i in l2:
            print(i,end=' ')
    def mark(a,name):
        if(name in l1):
            print(l2[l1.index(name)])
        else:
            print('Name not in list')
name=input('Student name to search:')
x=clas()
x.name(l1)
x.marks(l2)
x.mark(name)
