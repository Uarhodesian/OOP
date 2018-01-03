"""
 2. Create LinkedList Class with methods:
 a) get(i)
 b) put(i)
 c) delete(i)
 d) indexOf(el) - first element = el
 e) size()
 """

class employee:
    def __init__(self, fname, lname, salary, experiance, manager):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.experiance = experiance
        self.manager = manager
    
    def __str__(self):
        return "Hi! I am an employee"


class developer(employee):
    def __str__(self):
        return "Hi! I am a developer"


class designer(employee):
    def __init__(self, effect_coefficient):
        super().__init__(self, fname, lname, salary, experiance, manager)
        self.effect_coefficient = effect_coefficient
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
