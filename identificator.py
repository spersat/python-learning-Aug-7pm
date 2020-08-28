#identificator
a=5
b=5
print(id(a))
print(id(b)) # id(b) is the same as id(a)

#identificator lists: ids are differents even if content is the same
list1 = [1,2,3]
list2 = [1,2,3]
list3 = list1

print(id(list1))
print(id(list2)) # id(list1) different than id(list2)
print(id(list3)) # id(list3) same as id(list1)
