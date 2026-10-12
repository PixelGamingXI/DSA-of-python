from os import name


class Employee:
    def __init__(self, name, role, dept, salary):
        self.name = name
        self.role = role
        self.dept = dept
        self.salary = salary

    def Showdetails(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Department:", self.dept)
        print("Salary:", self.salary)



emp1 = Employee("Vinay Katore", "Software Engineer", "Google", 10000000)
emp1.Showdetails()