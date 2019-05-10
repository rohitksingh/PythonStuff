class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@mycompany.com"


emp1 = Employee('Rohit', 'Singh', 10000)
print(emp1.email)

