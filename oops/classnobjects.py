# Class and instance practice
# __init__(self) is nothing but constructor in java
# "self" is nothing but "this" keyword in java, it is convention to use "self"
# When we create a new object(instance) __init__ runs automatically
# Any functions that we create inside a class are called as methods of that particular class
# Employee is the class and emp1, emp2 are called as instances of the class "Employee"
# "fullname()" is the method of the "Employee" class

class Employee:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email
        
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname) # Now we can reuse it for every full name

emp1 = Employee("prasanth", "K", "kp@company.com") # this triggers __init__
emp2 = Employee("ajay", "A", "aa@company.com") # this triggers __init__

# print(emp2.fname)
# print(emp1.lname)

print(emp1.fullname()) # this triggers fullname()
