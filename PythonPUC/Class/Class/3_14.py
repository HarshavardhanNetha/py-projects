a=str(input("Name of the Item: "))
b=int(input("Value: "))
c=int(input("Quantity: "))
d=int(input("Discount = "))
t=int(input("Tax = "))
print("********BILL********")
print("Name of the item:",a)
print("Value of one item:",b)
print("Quantity:",c)
print("Actual Amount:",b*c)
temp=(b*c)*(100-d)/100
print("After Discount:",temp,"\n Tax=",temp*t/100)
print("-----------------------")
print("Amount to be Paid",temp*(100+t)/100)
print("-----------------------")
print("---THANK YOU - VISIT AGAIN---")