'''
##################### commands #######################"
id() --> to retrieve the info about the location of a data
print() --> to print info in the terminal
type() --> return the type of a variable

import keyword
print(keyword.kwlist)
--> return the list of the keywords (33) in python

##################### Rules #######################"
Identifiers:
The allowed start for an identifier name iq: a - z, A - Z, 0-9, _
Identifier should not start digit
Python programm/identifers are case sensitive
There are 33 keywords or reserved words that cannot be used for creating an identifier name
There is no lenght limit in Identifier

_a -->  protected variable (??)
__a  --> private variable (??)
__a___  ---> magic variable (??)


end operators
\n to go to the next line
end="" to don't go to the nextr line at the end of the print command
    print("Hello")
    print("I am good")
    --> Hello
        I am good
    print("Hello", end="")
    print("I am good")
    --> HelloI am good

##################### Operators #######################"
Arithmetic operaors
5+2: +, -, *, /, % and //, **

Relational operators
<, >, <=, >=, ==, !=
==> return a boolean (True or False)

Unary Operators
- , +


Assignmet Operators

Logical Operators
Identity Operators
bitwise Operators
Membership Operators


'''
print("hello", end="")
a=10
print (id(a))
print(a)
print("a")

a,b,c = 10,20,30
print(a,b,c)

age=60
job="developper"
salary="20000"

print('I am a {0}, my am {1} years old and my salary is {2}' .format(job,age,salary))



x = int(input("Please Enter First Number:"))
y = int(input("Please Enter Second Number:"))
print("Sum of two number:", x+y)

print("Sum of two numbers:", int(input("First Number"))+int(input("Enter Second Number")))
