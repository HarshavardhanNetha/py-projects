#wap function to calculate sum of elements in list or tuple
a=list('1234567')
print(a)
def sum_str(a):
    'sum of elements in list or tuple'
    sum=0
    for i in a:
        sum+=int(i)
    print(sum)
sum_str(a)
