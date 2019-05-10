class Employee:

    raise_amount = 1.04
    num_of_employee = 0;

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@mycompany.com"
        Employee.num_of_employee += 1

    def fullname(self):
        print(self.first+" "+self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * Employee.raise_amount)
        # This does not give ability to change for every instance


print("Initially num of empolyee: {}".format(Employee.num_of_employee))

emp1 = Employee('Rohit', 'Singh', 10000)
emp2 = Employee('Jon', 'Snow', 10)
Employee.raise_amount = 1.05
emp1.raise_amount = 1.03
print(emp1.raise_amount)                        # output = 1.03
print(emp2.raise_amount)                        # output = 1.05
print(Employee.raise_amount)                    # putput = 1.05

print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)

#     KEY
# is when we call emp1.raise_amount it checks if the
# attribute is present in the instance variable else it pulls
# that attribute from class

emp3 = Employee('Robert', 'Singh', 10000)
emp4 = Employee('Jon', 'Snow', 10)

emp3.raise_amount = 1.06
emp3.apply_raise()
print(emp3.pay)

# print("Now  num of empolyee: " + Employee.num_of_employee)

print("Now  num of empolyee: {}".format(Employee.num_of_employee))

