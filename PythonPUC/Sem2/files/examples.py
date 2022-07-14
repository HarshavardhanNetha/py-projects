>>> import os
>>> os.chdir(r'C:\Users\harsh\Desktop\pyt\Sem2\files')
>>> os.getcwd()
'C:\\Users\\harsh\\Desktop\\pyt\\Sem2\\files'
>>> os.mkdir('hello.txt')
>>> os.mkdir('hello')
>>> os.mkdir('hello')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    os.mkdir('hello')
FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'hello'
>>> os.path.exists('hello')
True
>>> os.rmdir(hello)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    os.rmdir(hello)
NameError: name 'hello' is not defined
>>> os.rmdir('hello')
>>> 
'''
first we open two arguments as str filename and mode
4 mides read-r write-w append-a create-x
f=open('hi.txt','x')
if file is not available..... it creates the file
f.close()
os.remove(filename) is to remove file nt dir.
'''
READING
1.Read file in single statement -- read function
f=open('hi.txt','r')
x=f.read()

2.first n char of file
f.read(5)
#if there are only 3 then NO ERROR it prints all 3

3.only one line line by line
f.readline() #prints first line
if repeated again it gives 2nd line and so on....
EOF error if file doesnt contaion repreated lines time

4.Loops
for i in f:
    print(x)    


Write mode append mode....
f=open('hi.txt',''w')
write clears all the data in it #previous content deletes
appennd mode adds the data
#explain about files in 4 ways of reading and 2 ways of writing

