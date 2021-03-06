class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return self.first+" "+self.last

    # Special Dunder methods
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        test = self.fullname()
        return len(test)

    def __repr__(self):
        return "{} - {}".format(self.first, self.pay)

    def __str__(self):
        return "Employee Details " \
               "\n------------------" \
               "\nName:{} {} \nPay:{}" \
               "\n------------------".format(self.first,self.last, self.pay)


emp2 = Employee('Jon', 'Snow', 500)
emp1 = Employee('Rohit', 'Singh', 10000)
print(emp1 + emp2)
print(len(emp1))
print(emp1)
print(str(emp2))
print(repr(emp2))