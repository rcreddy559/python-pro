class Employee:
    raise_amount = 3.09
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    def print_raise_amount(self):
        print(self.raise_amount)

emp = Employee("ravi", 30000)
Employee.set_raise_amount(2000) 
emp.print_raise_amount()
