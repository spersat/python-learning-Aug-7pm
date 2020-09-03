tuple12=()
tuple1=(10,20,30)
t2=10,20,30 # it is another way to create a tuple object, but not a best practice
#tuple1.append=(40) #not possible
print(tuple1)

t=(10)
print(type(t)) # for a single value tuple, it returns the type of the arg in the tuple. To have the tuple, need to put a ',' at the end of the tuple list
t1=(10,)
print(type(t1))

#slicing
#slicing [start_index : end_index]returns all the values between start_index and end_index-1
t=(10,20,30,40,50,60)
print(t[1:3]) # returns index 1 and 2
print(t[:]) # returns everything
print(t[3:]) # returns everything from index 3
print("hello")
