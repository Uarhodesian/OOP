"""
1. Create structure for department:
 a) There are 3 types of employee: developer, designer and manager
 b) Each employee has: first name, second name, salary, experiance (years) and manager
 c) Each designer has effectivness coefficient(0-1)
 d) Each manager has team of developers and designers.
 e) Department should have list of managers(which have their own teams)
 f) Department should be able to give salary (for each employee message: "@firstName@ @secondName@: got salary: @salaryValue@")
 g) Each employee gets the salary, defined in field Salary. If experiance of employee is > 2 years, he gets bonus + 200$, if experiance is > 5 years, he gets salary*1.2 + bonus 500
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
    def __str__(self):
        return "Hi! I am an employee"

class developer(employee):
    def __str__(self):
        return "Hi! I am a developer"
    
class designer(employee):
    def __init__(self, fname, lname, salary, experiance, manager, effect_coefficient):
        supper().__init__(self, fname, lname, salary, experiance, manager)
    
#anton = designer('Anton', 'Antonovich', 350, 2, 'Budkin')   
vasya = developer('Vasya', 'Pupkin', 300, 5, 'Budkin')
petya = developer('Petro', 'Petrovich', 200, 3, 'Budkin')

print(employee.number_of_employee)




#d    
class manager(employee):
    def __init__(self, effect_coefficient):
        pass
"""
    def count_square(self):
        return pi*self.x*self.y

    def __str__(self):
        return "Hi from circle!"


class Rectangle(Figure):
    def count_square(self):
        return self.x*self.y

    def __str__(self):
        return "Hi from rectangle!"

k = [1, "a"]

class SumError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


def double_sum(array):
    try:
        return summa(array)*2
    except SumError as err:
        print("Error occurred while trying to sum over: " + str(err))

def summa(array):
    try:
        a = 0
        print(a)
        for i in array:
            a = a+i
            print(a)
        return a
    except TypeError:
        raise SumError(array)

circle = Circle(1, 2)
dot = Dot(1, 2)
print(dot.x, dot.y)
print(dot)
print("Figure square: " + str(dot.count_square()))
print(circle)
print(type(circle))
double_sum(k)
"""
