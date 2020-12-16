class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first     # need not be the same
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)


    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000 )
emp_2 = Employee('Test', 'User', 60000)

print(len(emp_1))

#print(emp_1)

print(repr(emp_1))
print(str(emp_1))

#print(emp_1.__repr__())

print(emp_1 + emp_2)
