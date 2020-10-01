'''
def rem(n):
    return n%2
print(rem(9)) #return the remaining part of a division by n%2. Could be 0 or 1. Here 1

#lambda argument : express
rem = lambda n : n%2
print(rem(5))   # other way to do the same as the rem function

def multiply(x,y):
    return x*y
print(multiply(5,10)) #result: 50
'''

m = lambda x,y : x*y
print(m(2,3)) # other way to write the multiply function. returns 6
print(m(2,4)) # returns 8
