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


"""

单继承
https://www.auto-made.com/news/show-2533.html

"""


# class Person:
#     """父类，基类"""
#     Name = 'Person'
#
#     def sleep_info(self):
#         print('I am sleeping')
#
#
# class stu_info(Person):
#     """
#     子类、基类
#     """
#     school = 'School'
#
#     def learning_info(self):
#         print(self.Name)
#         self.sleep_info()
#         print('I am learning')
#
#
# daniel = stu_info()
# print(daniel.Name)
# daniel.learning_info()


"""
https://blog.csdn.net/liulanba/article/details/115372161
python3在父类的方法中调用子类重写的方法
"""

# class Father:
#     def func(self):
#         print(self.__class__)
#         print("Father")
#
#     def test_father(self):
#         print("Test_father", self.__class__)
#         # 子类的self调用的方法也是子类重写的方法
#         self.func()
#
#
# class Child(Father):
#     def func(self):
#         print(self.__class__)
#         print("Child")
#
#     def test_child(self):
#         # 子类的self是<class '__main__.Child'>
#         print("Test_child", self.__class__)
#         # 子类调用父类的方法
#         self.test_father()
#
#
# if __name__ == '__main__':
#     tes_c = Child()
#     tes_c.test_child()

from abc import ABC, abstractmethod  # 定义接口 Task (抽象基类)


class Task(ABC):
    @abstractmethod
    def execute(self):
        pass
    # 实现接口 Task 的 PrintTask 类


class PrintTask(Task):
    def execute(self):
        print("Executing Print Task")
    # 实现接口 Task 的 SaveTask 类


class SaveTask(Task):
    def execute(self):
        print("Executing Save Task")
    # 执行器类


class Executor:
    def execute_task(self, task: Task):
        task.execute()
    # 测试类


if __name__ == "__main__":
    # 创建任务
    print_task = PrintTask()
    save_task = SaveTask()
    # 创建执行器
    executor = Executor()
    # 执行任务
    executor.execute_task(print_task)
    executor.execute_task(save_task)
