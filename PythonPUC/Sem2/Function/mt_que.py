def geo(start, multiplier, length, i=0):
    if length <= 0:
        return    #or use a return statement
    x = start * multiplier ** i
    if(x<=length):
        print(x, "", end = "")
    geo(start, multiplier, length, i+1)
start = 1
multiplier =2
length = int(input()) 
i=0
geo(start, multiplier, length, i)
