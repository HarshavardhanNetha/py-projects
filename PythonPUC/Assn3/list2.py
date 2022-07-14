#Negative Index
list1=[1,2,3,4,5,6]
print(list1[-1])#6
print(list1[-len(list1)])
print(list1[1:-1])#2,3,4,5
print(list1[2:-2])#3,4
list1[2]=[7,8,9]
print(list1)# 1,2,[7,8,9],4,5,6
print(list1[2])#[7,8,9]
print(list1[2][1])# 8

