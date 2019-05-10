class Employee:
    raise_amount = 1.04
    num_of_employee = 0;

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@mycompany.com"

    def fullname(self):
        print(self.first+" "+self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


emp1 = Employee('Rohit', 'Singh', 10000)
emp2 = Employee('Jon', 'Snow', 10)
Employee.set_raise_amount(3.07)
print("Raise amount: {}".format(emp1.raise_amount))
emp1.set_raise_amount(2.05)
print("Raise amount: {}".format(emp2.raise_amount))
