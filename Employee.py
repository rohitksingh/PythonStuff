class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@mycompany.com"


    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp1 = Employee('Rohit', 'Singh', 10000)
print("Full name: "+emp1.fullname())


