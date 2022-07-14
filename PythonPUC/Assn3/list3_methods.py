list1=[1,2,3,4,1,2,1,1,2,4,5,6]
list1.append(10)#added 10 in end
print(list1)
print(list1.count(1))# return 1=appears in 4 times count(object)
print(list1.index(2))# returns index of fisrt occurance i.e 1(index(object)
print(list1.pop())# removes last element
print(list1)
print(list1.pop(0))# removes first elememt based on index
list1.remove(6)
print(list1)
list1.reverse()
print(list1)
list1.extend([20,30,40])
print(list1)
list1.insert(1,100)
print(list1)
