#operator is
# returns boolean (True or False)

a=50
b=a
print(a==b) #return True ==> == compares content of the object
print(a is b) # returns True ==> is compares object refs 

list1 = [1,2,"three"]
list2 = [1,2,"three"]

print(list1 == list2) # returns True as contents of list1 is the same as content of list2
print(list1 is list2) # returns False as object refs of list1 and list2 are different
print(id(list1))
print(id(list2))