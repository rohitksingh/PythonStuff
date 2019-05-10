class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@mycompany.com"

    def fullname(self):
        print(self.first + " " + self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_language):
        # self().__init__(self, first, last, pay)             this does not work in Python 2.7 but works in 3.0
        Employee.__init__(self, first, last, pay)
        self.prog_language = prog_language

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employee(self):
        for emp in self.employees:
            emp.fullname()





dev1 = Developer('Rohit', 'Singh', 10000, 'Java')
print(dev1.prog_language)

dev2 = Developer('Rohit1', 'Singh', 10000, 'Java')
dev3 = Developer('Rohit2', 'Singh', 10000, 'Java')
dev4 = Developer('Rohit3', 'Singh', 10000, 'Java')
dev5 = Developer('Rohit4', 'Singh', 10000, 'Java')
dev6 = Developer('Rohit5', 'Singh', 10000, 'Java')


manager = Manager('ManagerFname', 'ManagerLname', 10000, [dev1, dev2, dev3, dev4, dev5])
manager.print_employee()
