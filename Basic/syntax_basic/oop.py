import json

# class Employee:
#     def __init__(self, name, salary):
#         """
#         构造方法
#         :param name:
#         :param salary:
#         """
#         self.name = name
#         self.salary = salary
#
#     def func_1(self):
#         print(self)
#
#
# Employee1 = Employee('John', 100000)
# print(Employee1.name, Employee1.salary)
# # Employee1.func_1()
#
# # print(Employee.func_1(self))
# # #
# # #
# # # class Employee:
# # #     def __init__(self, name, salary):
# # #         # self.age = None
# # #         self.name = name
# # #         self.salary = salary
# # #
# # #     def printclass(self):
# # #         try:
# # #             return '{}'s salary is {}, and his age is {}'.format(self.name, self.salary, self.age)
# # #         except:
# # #             print("Error! No age")
# # #
# # #
# # # name = input()
# # # salary = (input())
# # # age = input()
# # #
# # # e = Employee(name, salary)
# #
# #
# # class exercise:
# #     def __init__(self, name, weight):
# #         self.name = name
# #         self.weight = weight
# #
# #     def running(self):
# #         self.weight -= 0.5
# #         print('名字为: {}，体重为{}'.format(self.name, self.weight))
# #
# #     def eating(self):
# #         self.weight += 1
# #         print('名字为: {}，体重为{}'.format(self.name, self.weight))
# #
# #
# # Daniel = exercise('Daniel', 75)
# # Daniel.eating()
# #
# #
# # class employee:
# #     EmpCount = 0
# #
# #     def __init__(self, name, age, years):
# #         self.name = name
# #         self.age = age
# #         self.years = years
# #         employee.EmpCount += 1
# #
# #     def display_info(self):
# #         print('员工姓名{} 年龄{} 年限{} 员工总人数为{}'.format(self.name, self.age, self.years, self.EmpCount))
# #
# #     def emp_rank(self):
# #         if self.years >=10:
# #             print('P1')
# #         elif self.years >5:
# #             print("P2")
# #         elif self.years >2:
# #             print("P3")
# #         else:
# #             print('P4')
# #
# #
# # a = employee('Alice', 36, 19)
# # b = employee('Bob', 31, 9)
# # c = employee('Apple', 27, 5)
# # print(employee.EmpCount)
# # a.display_info()
# # b.display_info()
# # c.emp_rank()
# #
# # print(employee.__dict__)
# # print(employee.__name__)
# # print(a.__dict__)
# # print(employee.__name__)
#
#
# """
#
# 单继承
# https://www.auto-made.com/news/show-2533.html
#
# """
#
#
# # class Person:
# #     """父类，基类"""
# #     Name = 'Person'
# #
# #     def sleep_info(self):
# #         print('I am sleeping')
# #
# #
# # class stu_info(Person):
# #     """
# #     子类、基类
# #     """
# #     school = 'School'
# #
# #     def learning_info(self):
# #         print(self.Name)
# #         self.sleep_info()
# #         print('I am learning')
# #
# #
# # daniel = stu_info()
# # print(daniel.Name)
# # daniel.learning_info()
#
#
# """
# https://blog.csdn.net/liulanba/article/details/115372161
# python3在父类的方法中调用子类重写的方法
# """
#
# # class Father:
# #     def func(self):
# #         print(self.__class__)
# #         print("Father")
# #
# #     def test_father(self):
# #         print("Test_father", self.__class__)
# #         # 子类的self调用的方法也是子类重写的方法
# #         self.func()
# #
# #
# # class Child(Father):
# #     def func(self):
# #         print(self.__class__)
# #         print("Child")
# #
# #     def test_child(self):
# #         # 子类的self是<class '__main__.Child'>
# #         print("Test_child", self.__class__)
# #         # 子类调用父类的方法
# #         self.test_father()
# #
# #
# # if __name__ == '__main__':
# #     tes_c = Child()
# #     tes_c.test_child()
#
# from abc import ABC, abstractmethod  # 定义接口 Task (抽象基类)
#
#
# class Task(ABC):
#     @abstractmethod
#     def execute(self):
#         pass
#     # 实现接口 Task 的 PrintTask 类
#
#
# class PrintTask(Task):
#     def execute(self):
#         print("Executing Print Task")
#     # 实现接口 Task 的 SaveTask 类
#
#
# class SaveTask(Task):
#     def execute(self):
#         print("Executing Save Task")
#     # 执行器类
#
#
# class Executor:
#     def execute_task(self, task: Task):
#         task.execute()
#     # 测试类
#
#
# if __name__ == "__main__":
#     # 创建任务
#     print_task = PrintTask()
#     save_task = SaveTask()
#     # 创建执行器
#     executor = Executor()
#     # 执行任务
#     executor.execute_task(print_task)
#     executor.execute_task(save_task)


"""
python中通常在属性和方法前加__(两条下划线)来进行属性和方法的隐藏。

特点：
1.在类外无法直接obj.__AttrName
2.在类内部可以直接使用obj.__AttrName
3.子类无法覆盖父类__开头的属性

方法和属性隐藏需要注意的地方：

1.外部不能直接饮用，需要对象._类__属性的形式可以提出隐藏的属性和方法
2.变形的过程只有在类的定义时发生一次，再次赋值时不会变形。
3.在继承中，如果父类不想让子类覆盖自己的方法，可以将方法定义为私有的。

"""


# class A:
#     def __init__(self, name, life):
#         self.__name = name
#         self.__life = life
#
#     def __run(self):
#         print('run')
#
#     def sing(self):
#         self.__run()
#         print('sing')
#
#
# b = A('daniel', 100)
# # b.sing()
# print(b._A__name)

"""
3.在继承中，如果父类不想让子类覆盖自己的方法，可以将方法定义为私有的。

"""

#
# class A:
#     def __fa(self):  # *_A__fa
#         print('from A')
#
#     def test(self):
#         self.__fa()  # 此时的fa方法是变形过的_A__fa,所以之行类A中的fa方法
#
#
# class B(A):
#     def __fa(self):  # *_B__fa
#         print('from B')
#         return "sss"
#
#
# b = B()
# print(b._B__fa())


"""
封装数据属性的意义：明确的区分内外，控制外部对隐藏的属性的操作行为


"""


