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
        if self.experiance > 5:
            self.salary = self.salary * 1.2 + 500
            return self.salary
        elif self.experiance > 2:
            self.salary = self.salary  + 200
            return self.salary
        else:
            return self.salary       
    def __repr__(self):
        return "employee('{}','{}','{}')".format(self.fname, self.lname, self.experiance)

    def __str__(self):
        return "Hi! I am an employee"

class developer(employee):
    number_of_developer = 0
    def __init__(self, fname, lname, salary, experiance, manager):
        employee.__init__(self, fname, lname, salary, experiance, manager)
        developer.number_of_developer += 1
    def __str__(self):
        return "developer"
    
class designer(employee):
    number_of_designer = 0
    def __init__(self, fname, lname, salary, experiance, manager, effect_coefficient):
        #supper().__init__(self, fname, lname, salary, experiance, manager)
        employee.__init__(self, fname, lname, salary, experiance, manager)
        self.effect_coefficient = effect_coefficient
        designer.number_of_designer += 1
    def full_salary(self):
        self.salary = self.salary * self.effect_coefficient
        return self.salary
    def __str__(self):
        return "designer"
    
class manager(employee):
    count_dev = 0
    count_des = 0

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

    def print_emp(self):
            for employees in self.employees:
                print('--->', employees)

    def count_emp(self):
            for employees in self.employees:
                if isinstance(employees, designer):
                    self.count_des += 1
                elif  isinstance(employees, developer):
                    self.count_dev += 1
             
                 
vova = developer('Vova', 'Pu', 300, 7, 'Budkin')                
anton = designer('Anton', 'Antonovich', 350, 2, 'Budkin', 1)   
vasya = developer('Vasya', 'Pupkin', 300, 5, 'Budkin')
petya = developer('Petro', 'Petrovich', 200, 3, 'Budkin')
maria = designer('Maria', 'Antonovich', 200, 1, 'Budkin', 0.7)        
Budkin = manager('Vasya', 'Budkin', 300, 10, 'Boss', ['vova', 'anton', 'petya', 'maria'])
zhuk = manager('Mykola', 'Zhuk', 500, 12, 'Boss', ['Budkin'])     

print(employee.number_of_employee)
print(designer.number_of_designer)
print(developer.number_of_developer)
print(anton.__repr__())
print(anton.full_salary())
print(Budkin.__repr__())
print(Budkin.full_salary())
print(Budkin.count_emp)
print(Budkin.print_emp())

#print(Budkin.count_emp)
