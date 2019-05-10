class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@mycompany.com"

    def fullname(self):
        print(self.first+" "+self.last)


emp1 = Employee('Rohit', 'Singh', 10000)
emp2 = Employee('Jon', 'Snow', 10)
print(emp1.fullname())
print(Employee.fullname(emp2))






