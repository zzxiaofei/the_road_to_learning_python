# NP 98
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def printclass(self):
#         try:
#             print('{} salary is {}, and his age is {}'.format(self.name, self.salary, self.age))
#
#         except:
#             print('Error! No age')
#
#
# e = Employee(input(), input())
# e.printclass()
# e.age = input()
# e.printclass()


# NP 99

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def printclass(self):
#         print('{}‘s salary is {}, and his age is {}'.format(self.name, self.salary, self.age))
#
#
# name = input().strip()
# salary = int(input().strip())
# age = int(input().strip())
# e = Employee(name, salary)
#
# has_age = hasattr(e, 'age')
# print(has_age)
# if not has_age:
#     setattr(e, 'age', age)
#
# e.printclass()


# NP100 重载预算

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print(f'({self.x}, {self.y})')

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)


x, y = map(int, input().split())
c1 = Coordinate(x, y)
x, y = map(int, input().split())
c2 = Coordinate(x, y)

c3 = c1.__add__(c2)
c3.__str__()
