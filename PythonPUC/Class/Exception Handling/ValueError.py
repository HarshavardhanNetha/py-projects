import sys
try:
    print(int('one'))
except:
    print('Type Error')
    print(sys.exc_info())
finally:
    print('Last Statement')
