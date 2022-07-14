#wap to delete the puctuations from the given string
a=input()
s='!@#$%^&*()<>?/\';:\"[]{}-=_+'
s1=''
for i in a:
    if i not in s:
        s1+=i
print(s1)
