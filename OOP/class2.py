class emp_Data:
    '''Employee Data'''
    company_name = 'IBM' # static variable
    def __init__(self,name,age): #constructor, instance method
        self.name = name #instance variable
        self.age = age
   
    def emp_Details(self): #local method
        a=100 #local variable
        print("Employee Name", self.name)
        print("Employee Age", self.age)
    



emp = emp_Data('Narasimha Reddy', 37)
emp.emp_Details()

emp2 = emp_Data('Raj', 38)

emp2.emp_Details()


#this, current obj - JAva, Javascript
#self in python - current object