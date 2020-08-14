'''
username=input("Enter your username: ")
password=input("Enter your password: ")
if(username=="Seb" and password=="123"):
    print ("successfully connected")
else:
    print ("Login failed - Please enter correct login and password")
'''
# x = not ""
# print(x)

'''
For non boolean types, example
0, empty --> false
value --> true

for and 
    if x is false, result is x --> 0
    if x is true, result is y --> "Hi"
'''
x = 0 and ()
y = 1 and ()
z = 0 and (1,2)
a = 1 and (1,2)
print("x = 0 and () returns for x:", x)      # 0
print("y = 1 and () returns for y:", y)      # ()
print("z = 0 and (1,2) returns for z:", z)   # 0
print("a = 1 and (1,2) returns for a:", a)   # (1, 2)
'''
for or
    example
    if x is false, result is y
    if x is true, result is x
'''
x = 0 or ()
y = 1 or ()
z = 0 or (1,2)
a = 1 or (1,2)
print("x = 0 or () returns for x:", x)      # ()
print("y = 1 or () returns for y:", y)      # 1
print("z = 0 or (1,2) returns for z:", z)   # (1,2)
print("a = 1 or (1,2) returns for a:", a)   # 1

