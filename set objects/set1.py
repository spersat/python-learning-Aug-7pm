#create empty set object
#operations allowed with set
'''
add()
remove() --> returns an error if the element is not in the set list
union()
discard() --> does not returns an error in case element is not in the set list
pop() --> remove one element of the set randomly

'''

s=set()
print(s)
s.add(10)
print(s)

s1={10,20,30,'USA'}
x=s1.pop()
print(s1)
print(x)