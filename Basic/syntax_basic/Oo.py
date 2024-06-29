# # # class Employee:
# # #     def __init__(self, name, salary):
# # #         """
# # #         构造方法
# # #         :param name:
# # #         :param salary:
# # #         """
# # #         self.name = name
# # #         self.salary = salary
# # #
# # #     def func_1(self):
# # #         print(self)
# # #
# # #
# # # Employee1 = Employee('John', 100000)
# # # print(Employee1.name, Employee1.salary)
# # # # Employee1.func_1()
# # #
# # # # print(Employee.func_1(self))
# #
# #
# # class Employee:
# #     def __init__(self, name, salary):
# #         # self.age = None
# #         self.name = name
# #         self.salary = salary
# #
# #     def printclass(self):
# #         try:
# #             return '{}'s salary is {}, and his age is {}'.format(self.name, self.salary, self.age)
# #         except:
# #             print("Error! No age")
# #
# #
# # name = input()
# # salary = (input())
# # age = input()
# #
# # e = Employee(name, salary)
#
#
# class exercise:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#     def running(self):
#         self.weight -= 0.5
#         print('名字为: {}，体重为{}'.format(self.name, self.weight))
#
#     def eating(self):
#         self.weight += 1
#         print('名字为: {}，体重为{}'.format(self.name, self.weight))
#
#
# Daniel = exercise('Daniel', 75)
# Daniel.eating()
#
#
# class employee:
#     EmpCount = 0
#
#     def __init__(self, name, age, years):
#         self.name = name
#         self.age = age
#         self.years = years
#         employee.EmpCount += 1
#
#     def display_info(self):
#         print('员工姓名{} 年龄{} 年限{} 员工总人数为{}'.format(self.name, self.age, self.years, self.EmpCount))
#
#     def emp_rank(self):
#         if self.years >=10:
#             print('P1')
#         elif self.years >5:
#             print("P2")
#         elif self.years >2:
#             print("P3")
#         else:
#             print('P4')
#
#
# a = employee('Alice', 36, 19)
# b = employee('Bob', 31, 9)
# c = employee('Apple', 27, 5)
# print(employee.EmpCount)
# a.display_info()
# b.display_info()
# c.emp_rank()
#
# print(employee.__dict__)
# print(employee.__name__)
# print(a.__dict__)
# print(employee.__name__)



