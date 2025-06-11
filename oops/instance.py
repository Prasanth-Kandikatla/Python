# Class variables and instance variables
# We call class variables as class attributes
# If we want to manage particular instance then it is recommended to use "self.attribute"
# If we want to manage all instances same, we should use "Employee.attribute"

class Employee:

    employee_num = 0
    amount_increased = 1.05
    def __init__(self, fname, lname, email, sal):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.sal = sal

        self.employee_num += 1

        
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname) # Now we can reuse it for every full name

    def sal_raise(self):
        self.sal = int(self.sal * Employee.amount_increased)

emp1 = Employee("prasanth", "K", "kp@company.com", 100000) # this triggers __init__
emp2 = Employee("ajay", "A", "aa@company.com", 50000) # this triggers __init__

# print(emp1.__dict__)
# print(emp1.sal)
# emp1.amount_increased = 1.10
# emp1.sal_raise()

# print(emp1.sal)
# print(emp1.__dict__)

print(Employee.employee_num)



