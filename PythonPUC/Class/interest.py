p=int(input("Priciple Amount:"))
t=int(input("Time:"))
r=int(input("Rate of Interest:"))
si=(p*t*r)/100
ci=p*((1+r/100)**t)
print("Simple Interst =",si)
print("Total Money to be paid =",int(p+si))
print("Compound Interset =",round(ci,2))
#here round determines the no od digits to be print after decimal point
print("Total Money to be paid =",int(p+ci))
