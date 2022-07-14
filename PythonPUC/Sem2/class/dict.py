#create a dict with names and ages of the persons with n size frm user
#write a function called print age inside the class called age with 2 parameter strng and dict
#print age of the person based on name
'''read dict with names and ages of persons woth user defined names and inputs'''
d={}
x=int(input('Size of dict:'))
for i in range(x):
    a=input('Name:')
    b=int(input('Age:'))
    d[a]=b
class dict:
    def age(a,b):
        if(b in d.keys()):
            print(d[b])
        else:
            print('No name')

name=input('Enter name to search age:')
#d=input('In which dict you wanna check:')
x=dict()
x.age(name)
