import datetime


class Employee:
    number_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first.lower()}.{last.lower()}@company_name.com'

        Employee.number_of_employees += 1

    def fullname(self):
        return f'{self.first.capitalize()} {self.last.capitalize()}'

    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_pay_raise(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day):
        if day.weekday() in [5, 6]:
            return False
        else:
            return True


emp1 = Employee('Jack', 'Smith', 2000)
emp2 = Employee('Mary', 'Gold', 3000)


# emp_str1 = 'Bob-Summers-1000'
# emp3 = Employee.from_string(emp_str1)
# print(emp3.__dict__)
# print(Employee.number_of_employees)
#
# print(emp3.fullname())
# print(emp3.email)

# print(Employee.is_workday(datetime.date.today()))
# print(emp1.is_workday(datetime.date.today()))


def my_decorator(f):
    print('Staring')
    f()
    print('Ended')


@my_decorator
def say_hello():
    print('Hello!')


say_hello
