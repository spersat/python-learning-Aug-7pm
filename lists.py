#list
'''
    creation: list1=[]
    add element: list1.append(<value>) --> add an element at the end of the list
    remove an element: list.remove(<value>) --> remove the first occurence of the element in the list
    delete a list: del (name of the list)
    delete an element: del(name of the list[index of the element to delete])
    sort() descending or ascending
    pop() --> remove the last element of the list
    replace() --> list1[3]=20 --> replace in list1 the value in the index 3 by 20 
    insert() --> insert an element in a specific position ex:list1.insert(0,10) --> insert 10 in the 1st place
    count()
    reverse: --> reverse the list
    clear(name of the list) --> clear all the values inside a list
    copy()
    min(name of the list) --> find the min of trhe list. Works only with similar elements
    max(name of the list) --> find the max of trhe list. Works only with similar elements
    count --> count number of occurances in a list (coutn)

    indexing: returns a single value. TIP: a[-1] returns the last value of the list
    slicing: 


list1=[]
list1.append(10)
list1.append("test")
list1.append(20)
list1.append(10)
print (list1) #print all the list
print(list1[2]) #print one specif element of the list, starting from index 0
list1.remove(20)
print (list1)
del(list1[1])
print (list1)

list1.insert(8,100)
print (list1)

# to check if a value exists in a list we use the "in" function
'''
a=[10,20,30,40,50]
if 20 in a:
    print("20 is present")
print(a[4])
print([a[1:10]])
print([a[1:4]])

#slicing
print(a[ : ]) # return the complete list
print([a[1:5]]) #return values in indexes 1, 2, 3 and 4 --> 20, 30, 40, 50 
print(a[1:5:2]) #return values in indexes 1 and 3 --> 20, 40
#indexing
print(a[2])
a.reverse()
print(a)
