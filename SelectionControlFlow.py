'''
Selection control flow
If
If else
If elif else

blocks of actions are defined with the indentation
'''
i=10
if i>5:
    print("Hello1")
    print("Hello2")
    print("Hello3")
else:
    print("Hello4")
    print("Hello5")

'''
n=int(input("Please enter a number  between 0 and 5: "))
if n == 0:
    print("Zero")
elif n==1:
    print("one")
elif n==2:
    print("two")
elif n==3:
    print("three")
else:
    print("after three")
'''
list1 = ["","one","two","three","four","five","six","seven","eigth","nine","ten","Eleven","Twelve","Thirteen","Fourteen","fiveteen","Sixteen","Seventeen","Eighteen","nineteen"]
list2 = ["","","twenty","thirty"]
n = int(input("Please enter number: "))
if n==0:
    print("Zero")
elif n <=10:
    print(list1[n])
else:
    j=n//10
    k=n%10
    print(list2[n//10] + '' + list1[n%10])

