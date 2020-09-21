'''
def fact(n):
    if n==1:
        return n
    else:
        return  n*fact(n-1)

print(fact(5))

i=0
def order():
    global i
    i+=1
    print('Order Successfully created',i)
    order()
    
order() # returns Order Successfully created 1, then 2, then 3.... 

i=0
def order():
    global i
    i+=1
    print('Order Successfully created',i)
    order()
    
order() # returns Order Successfully created 1, then 2, then 3.... 

#disadvatages
#1.recursion logic, might be hard to understand
#2.debugging problemm
#3.lot memory and time

def order():
    print('Order Successfully created')
    order()
    
order() # returns "Order Successfully created multiple" times
'''
  
import keyword
print(len(keyword.kwlist)) # reurns number of keywords in the keyword list element
print(keyword.kwlist) #returns the list of keyword
