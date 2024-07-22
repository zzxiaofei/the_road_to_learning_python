"""
https://www.nowcoder.com/exam/oj?page=1&tab=Python%E7%AF%87&topicId=314
Python入门练习
"""

# class Player:
#     def __init__(self, name, items=[]):
#         self.name = name
#         self.items = items
#
#
# p1 = Player("John")
# p2 = Player("Bob")
# p3 = Player("Sally", items=["sword"])
#
# p1.items.append("armor")
# p2.items.append("sword")
#
# print(p1.items)


# a = None
#
# if a:
#     print("Not None")
# if a == None:
#     print("None")
# if a is None:
#     print("None")


"""No.28"""

# num = input()
# new_list = []
# for i in num:
#     number = (int(i) + 3) % 9
#     new_list.append(number)
# new_list[0], new_list[2] = new_list[2], new_list[0]
# new_list[1], new_list[3] = new_list[3], new_list[1]
# for i in new_list:
#     print(i, end='')


"""No.29"""
#
# num = int(input())
# stack = [1, 2, 3, 4, 5]
# first = stack.pop()
# print(stack)
# second = stack.pop()
# print(stack)
# third = stack.append(1)
# print(stack)

"""No.30"""
queue = [1, 2, 3, 4, 5]
for num in range(2):
    queue.append(0)
    print(queue)
numbers = int(input())
queue.append(numbers)
print(queue)
"""No.98"""
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

# class Coordinate:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         print(f'({self.x}, {self.y})')
#
#     def __add__(self, other):
#         return Coordinate(self.x + other.x, self.y + other.y)
#
#
# x, y = map(int, input().split())
# c1 = Coordinate(x, y)
# x, y = map(int, input().split())
# c2 = Coordinate(x, y)
#
# c3 = c1.__add__(c2)
# c3.__str__()
