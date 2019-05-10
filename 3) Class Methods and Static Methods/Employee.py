import datetime


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

    @classmethod
    def from_string(cls,record):
        first, last, pay = record.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return True
        return False


emp1 = Employee('Rohit', 'Singh', 10000)
emp2 = Employee('Jon', 'Snow', 10)
Employee.set_raise_amount(3.07)
print("Raise amount: {}".format(emp1.raise_amount))
emp1.set_raise_amount(2.05)
print("Raise amount: {}".format(emp2.raise_amount))

# Using class metgjod to create alternate constructor
record = 'Bruce-Wayne-2000'
first, last , pay = record.split('-')
emp3 = Employee(first, last, pay)
print(emp3.__dict__)

# instead now we can use a class method
emp5 = Employee.from_string('Lady-Gaga-90')
print(emp5.__dict__)

# Key things
# 1) How to create a class method
# 2) Use of cls()

# Instance Variable methods pass self, Class methods pass cls, and static method dont pass anything

# Use of static method?
# method which has some logical connection with class but does not actually depend on class instance

my_birthday = datetime.date(2019, 5, 10)
print(Employee.is_work_day(my_birthday))

