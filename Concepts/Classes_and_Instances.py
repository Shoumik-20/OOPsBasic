# Python Object Oriented

class Employee:

    def __init__(self, first, last, pay):
        self.first = first     #need not be the same
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
emp_1 = Employee('Corey', 'Schafer', 50000 )
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname()) # calling method in instance . No need of passing an argument 
print(emp_2.fullname())

print(Employee.fullname(emp_1)) # calling method in class
