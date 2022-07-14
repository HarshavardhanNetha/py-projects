import math
import sys
a=[4,8,-3,5]
for i in a:
    try:
        b=math.factorial(i)
    except:
        print(sys.exc_info())
    else:
        print(b)
