"""
1. Create structure for department:
 a) There are 3 types of employee: developer, designer and manager
 b) Each employee has: first name, second name, salary, experiance (years) and manager
 c) Each designer has effectivness coefficient(0-1)
 d) Each manager has team of developers and designers.
 e) Department should have list of managers(which have their own teams)
 f) Department should be able to give salary (for each employee message: "@firstName@ @secondName@: got salary: @salaryValue@")
 g) Each employee gets the salary, defined in field Salary. If experiance of employee is > 2 years, he gets bonus + 200$,
    if experiance is > 5 years, he gets salary*1.2 + bonus 500
 h) Each designer gets the salary = salary*effCoeff
 i) Each manager gets salary +
   ii) 200$ if his team has >5 members
   iii) 300$ if his team has >10 members
   iiii) salary*1.1 if more than half of team members are developers.
 j) Redefine string representation for employee as follows:
"@firstName@ @secondName@, manager:@manager secondName@, experiance:@experiance@"
 """
class employee:
    number_of_employee = 0
    def __init__(self, fname, lname, salary, experiance, manager):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.experiance = experiance
        self.manager = manager
        employee.number_of_employee += 1
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    def full_salary(self):
        ratio = 1
        if experiance > 2:
            self.salary = self.salary * self.effect_coefficient
        elif experiance > 5:
            self.salary = self.salary * self.effect_coefficient
    def __repr__(self):
        return "employee('{}','{}','{}')".format(self.fname, self.lname, self.experiance)          
    def __str__(self):
        return "Hi! I am an employee"

class developer(employee):
    def __str__(self):
        return "Hi! I am a developer"
    
class designer(employee):
    def __init__(self, fname, lname, salary, experiance, manager, effect_coefficient):
        #supper().__init__(self, fname, lname, salary, experiance, manager)
        employee.__init__(self, fname, lname, salary, experiance, manager)
        self.effect_coefficient = effect_coefficient
    def full_salary(self):
        self.salary = self.salary * self.effect_coefficient

class manager(employee):
    def __init__(self, fname, lname, salary, experiance, manager, employees=None):
        employee.__init__(self, fname, lname, salary, experiance, manager)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

        def add_emp(self, emp):
            if emp not in self.employees:
                self.employees.append(emp)

        def remove_emp(self, emp):
            if emp in self.employees:
                self.employees.remove(emp)

        def print_emps(self):
            for emp in self.employees:
                print('--->'.emp.fullname())

class department(manager):
    def __init__(self, fname, lname, manager=None):
        employee.__init__(self, fname, lname)
        if manager is None:
            self.manager = []
        else:
            self.manager = manager

        def add_man(self, man):
            if man not in self.manager:
                self.manager.append(man)

        def remove_man(self, man):
            if emp in self.manager:
                self.manager.remove(man)

        def print_man(man):
            for man in self.manager:
                print('--->'.man.fullname())
                
anton = designer('Anton', 'Antonovich', 350, 2, 'Budkin', 1)   
vasya = developer('Vasya', 'Pupkin', 300, 5, 'Budkin')
petya = developer('Petro', 'Petrovich', 200, 3, 'Budkin')
maria = designer('Maria', 'Antonovich', 200, 1, 'Budkin', 0.7)   
Budkin = manager('Vasya', 'Budkin', 300, 10, 'Boss')
zhuk = manager('Mykola', 'Zhuk', 500, 12, 'Boss')
print(employee.number_of_employee)
print(anton.__repr__())
