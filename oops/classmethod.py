# Python have 3 types of methods
# Regular, Class and Static methods
# Regular and class methods both are declared inside the class but class method is decorated with "@classmethod"
# Class method is something that's used to manage class variables

class Employee:

    employee_num = 0
    amount_increased = 1.04
    def __init__(self, fname, lname, email, sal):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.sal = sal

        Employee.employee_num += 1

        
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname) # Now we can reuse it for every full name

    def sal_raise(self):
        self.sal = int(self.sal * Employee.amount_increased)

    @classmethod
    def raise_amt(cls, amount):
        cls.amount_increased = amount

    @classmethod #It is called as creating Alternative Constructor
    def create_emp(cls, eemp):
        first, last, eemail, saly = eemp.split('-')
        return Employee(first, last, eemail, saly)

    @staticmethod #Static method does not deal with any of the class or instance variables
    def isworkday(day):
        if day == 5 or day == 6: #Say 0 till 4 are Monday through Friday
            print(False)
        else:
            print(True)

    #Here static method is nowhere related to class or instance variables
emp1 = Employee("prasanth", "K", "kp@company.com", 100000) 
emp2 = Employee("ajay", "A", "aa@company.com", 50000) 

emp1_str = 'John-T-jt@company.com-60000'
emp2_str = 'Ravi-P-pr@company.com-80000'


new_emp1 = Employee.create_emp(emp1_str)
new_emp2 = Employee.create_emp(emp2_str)

print(Employee.isworkday(4))

# print(new_emp2.email)
# print(new_emp2.fname)
# print(new_emp2.sal)

# print(new_emp1.employee_num)
# emp1.raise_amt(1.05)
# print(Employee.amount_increased)
# print(emp1.amount_increased)
# print(emp2.amount_increased)
