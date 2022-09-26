class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first.lower()}.{last.lower()}@company_name.com'

    def fullname(self):
        return f'{self.first.capitalize()} {self.last.capitalize()}'

    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees:
            self.employees = employees
        else:
            self.employees = []

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print(emp.fullname())


emp1 = Employee('Jack', 'Smith', 2000)
emp2 = Employee('Mary', 'Gold', 3000)

dev1 = Developer('Bob', 'Summers', 1000, 'Python')
man1 = Manager('Sarah', 'Watson', 5000)
# man1.add_employee(dev1)
# man1.add_employee(emp1)
# man1.add_employee(emp2)
# man1.print_employees()

# print(isinstance(man1, Manager))     # True
# print(isinstance(man1, Developer))   # False

# print(issubclass(Manager, Employee))  # True
# print(issubclass(Employee, Manager))  # False
