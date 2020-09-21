import math

print (math.sqrt(100))

def emp_details(name, age):
    x='My name is:  ' +name
    y='My age is: ' +str(age)
    return x,y

a=emp_details('Sebastien',38)

print(a) # returns a tuple ('My name is:  Sebastien', 'My age is: 38') if multiple output, if not just the line

def multiple(*a):
    a=a
    return a

print(multiple('Seb', 38, 38, 'Paris')) # returns ('Seb', 38, 38, 'Paris')

def other(a,*b):
    a=a
    return a

print(other('Seb', 38, 38, 'Paris')) # returns Seb

def other(a,*b):
    b=b
    return b

print(other('Seb', 38, 38, 'Paris')) # returns (38, 38, 'Paris')



