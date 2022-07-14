a=[1,2,3,4,5]
import sys
try:
    print(a+2)
except IndentationError:
    print('Intendation Error')
except IndexError:
    print('Index Error')
except:
    print(sys.exc_info())
else:
    print(b)
print('#Final')
