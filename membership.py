# membership operator
# returns True if string is part of the text source
# returns False if string is not part of the text source

str1 = "Hi, my name is sebastien, I am the gretest man in the world"
print("name" in str1) # check if name is in str1 --> yes so True
print("ariane" in str1) # check if ariane is in str1 --> no so False

set1 = {1,2,3,3,4}
print("one" in set1)

student_name = ["Alpha", "Beta", "Gamma"]
print("Alpha" in student_name) # True
print("alpha" in student_name) # False --> case sensitive