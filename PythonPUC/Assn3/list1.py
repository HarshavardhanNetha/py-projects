list1=[1,2,3,4,5,6,7,8,9,10]
print(list1)
#print(list1[:])
#for i in list1:
#	print(i,end=" ")
print(len(list1))# 10
print(list1[2:5])#3,4,5
print(list1[:2])# 1,2
print(list1[::2])#1,3,5,7,9
print(list1[2:])#3,4,5,6,7,8,9,10
print(list1[2::])#3,4,5,6,7,8,9,10
print(min(list1))#1
print(max(list1))#10
print(sum(list1))#55
print(1 in list1)# true
print(11 not in list1)# true
list1[9]=11
print(list1)
del list1[9]#1,2,3,4,5,6,7,8,9
print(list1)
list1.append(10)
print(list1)#1,2,3,4,5,6,7,8,9,10
list1.insert(9,11)
print(list1)#1,2,3,4,5,6,7,8,9,11,10
print(all(list1))# true if any element is 0 it gives false
print(any(list1))
list2=list("sreedhar")
print(list2)
print(sorted(list2))# returns sortd list but original list not modified
list2.sort()
print(list2)# sorted and modify original list
list3=[11,12,13]
list4=[14,15,16]
print(list3+list4)
print(list3*2)
list5=list4
print(list5)
list6=list1[:4]
print(list6)

