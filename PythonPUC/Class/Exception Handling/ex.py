a=[1,2,3,4,5]
try:
    b=a[6]
    print(a[2])
except IndentationError:
    print('Intendation Error')
except IndexError:
    print('Index Error')
else:
    print(b)
print('#Final')
