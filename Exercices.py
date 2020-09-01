'''
#exercice 1
x = int(input("enter a value: "))
for i in range (x):
    print('*', end=" ")

#exercice 2
x = int(input("enter a value: "))
for i in range(x):
    print("A "*x, end = " ")
    print("")

#exercice 3
x = int(input("enter a value: "))
for i in range(x):
    print("* "*x, end = " ")
    print("")

#exercice 4
x=int(input("Enter a value: "))
for i in range(x):
    print((str(x)+ " ")*x)

#exercice 5
x=int(input("Enter a value: "))
for i in range(x):
    print(str(i+1)*x)

#exercice 6
x=int(input("Enter a value: "))
for i in range(x):
    print(str(x-i)*x)

#exercice 7
x=int(input("Enter a value: "))
for i in range(x):
    print('* '*(i+1))

#exercice 8
x=int(input("Enter a value: "))
for i in range(x):
    print('A '*(i+1))

#exercice 9
x=int(input("Enter a value: "))
for i in range(x):
    print('A '*(x-i))

#exercice 10
x=int(input("Enter a value: "))
for i in range(x):
    print((chr(65+i)+" ")*(i+1))

#exercice11
x=int(input("Enter a value: "))
for i in range(x):
    print((str(i+1)+" ")*(i+1))

#exercice12
x=int(input("Enter a value: "))
for i in range(x):
    for j in range (i+1):
        print (j+1, end=" ")
    print("")

#exercice 13
x=int(input("Enter a value: "))
for i in range(x):
    for j in range (i+1):
        print (chr(65+j), end=" ")
    print("")

#exercice 14
x=int(input("Enter a value: "))
for i in range(x):
    for j in range (x-i):
        print (str(j+1), end=" ")
    print("")

#exercice 15
x=int(input("Enter a value: "))
for i in range(x):
    if (i==0 or i==x-1):
        print ("* "*x)
    else:
        print("* " + "  "*(x-2) + "*")

#exercice 16
x=int(input("Enter a value: "))
for i in range(x):
    for j in range (x-i):
        print (chr(65+j), end=" ")
    print("")

#exercice 17
x=int(input("Enter a value: "))
for i in range(x):
    for j in range (x-i):
        print (str(x-j), end=" ")
    print("")

#exercice 18
x=int(input("Enter a value: "))
for i in range(x):
    for j in range (x-i):
        print (chr(64+(x-j)), end=" ")
    print("")

#exercice 19
str1=input("Enter a string: ")
x=len(str1)
for i in range(x):
    for j in range (i+1):
        print(str1[j], end="")
    print("")

#exercice 20
x=int(input("Enter a value: "))
k=0
for i in range (x):
    for j in range (i+1):
        print (chr(65+k), end="")
        k=k+1
    print("")

#exercice 21
x=int(input("Enter a value: "))
k=1
for i in range (x):
    for j in range (i+1):
        print (str(k) + " ", end="")
        k=k+1
    print("")

#exercice 22
x=int(input("Please enter a value: "))
for i in range (x):
    for j in range (i+1):
        if j == 0:
            print(str(i+1)+ " ", end= "")
            k=i+x-j
        if j> 0:
            print(str(k)+ " ", end= "")
            k=k+x-j-1
    print("")

#exercice 23
x=int(input("Please enter a value: "))
for i in range (x):
    for j in range (i+1):
        if j == 0:
            print(chr(65+i)+ " ", end= "")
            k=i+x-j
        if j> 0:
            print(chr(64+k)+ " ", end= "")
            k=k+x-j-1
    print("")
'''
#exercice 24

