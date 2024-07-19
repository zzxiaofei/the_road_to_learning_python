import math
import logging
import time

""" 
向函数传递信息 
    :parameter username: 形参
    :实参
    :传参
"""

# def func_practice(username):

#     # print(f"Hello,{username.title()}")
#     print('Hello,{}'.format(username.title()))
#
#
# func_practice('Daniel')  # :argument Daniel: 实参


# def favorite_book(book_name):
#     print("I love " + book_name)
#
#
# def describe_pet(animal_type, pet_name):
#     print(f"I have a {animal_type}")
#     print(f"My {animal_type}'s nam is {pet_name.title()}")
#
# favorite_book('我的地坛')
# describe_pet('dog', 'dudu')


"""
    1.return不是必要部分，return关键字可以省略
    2.return是函数体的结束标志，return后面的语句块不会执行，函数认为到 return就结束了
    3.return有返回值时，在调用函数时需要用一个变量来接收
    4.return后面没有任何值，则默认返回None

"""

"""
1. 位置参数
2. 指定参数：参数名=参数值
3. 缺省参数：定义函数的时候，在参数列表中给参数赋了默认值
4. 不定长参数：*和**可以不定长度的实参
    : *args: 多个参数存在一个元组中，调用函数只能是位置传参
    : **kwargs:多个参数存在一个字典里，调用函数只能是指定传参
"""


# def fun1(*args):
#     print(args)
#     print(type(args))
#     sum_1 = 0
#     for arg in args:
#         sum_1 = sum_1 + arg
#     print(f"The sum of {sum_1}")
#
#
# def fun2(**kwarg):
#     print(kwarg)
#     print(type(kwarg))
#
#
# fun1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# fun2(name='name', h='18')
# fun2(city='city', country='country')


# # def fun3(n):
# #     """
# #     循环实现递归
# #     :param n:
# #     :return:
# #     """
# #     sum_1 = 1
# #     for i in range(1, n + 1):
# #         # print(i)
# #         sum_1 = sum_1 * i
# #     return sum_1
# #
# #
# # res = fun3(5)
# # print(res)
#
#
# def fun4(n):
#     """
#     递归函数：函数调用自己本身，有结束条件
#     :param n:
#     :return:
#     """
#     if n == 1:
#         return 1
#     else:
#         return n * fun4(n - 1)
#
# res = fun4(5)
# print(res)

#
#
# """
#     匿名函数
# """
#
#
# #
# # res = lambda m: m ** 2
# # print(res(10))
# #
# # res_new = lambda *args: sum(args)
# # print(res_new(1, 2, 3, 4, ))
# #
# #
#
#
# def log_info(fun):
#     """
#     封装一个日志打印方法
#     :param fun:
#     :return:
#     """
#
#     def wrapper():
#         logging.warning('{}函数正在执行中'.format(fun.__name__))
#         start_time = time.time()
#         fun()
#         end_time = time.time()
#         run_time = end_time - start_time
#         logging.warning('{}函数的执行时间为{}'.format(fun.__name__, run_time))
#
#     return wrapper
#
#
# @log_info
# def func5():
#     # time.sleep(2)
#     print('hello world')
#
#
# func5()
#
#
# def rabit(n):
#     if n == 1:
#         return 2
#     elif n == 2:
#         return 3
#     else:
#         return rabit(n - 1) + rabit(n - 2)
#
#
# # 2, 3, 5, 8, 13
#
# a = int(input())
# b = rabit(a)
# print(b)
#
# # f(2) = f(2-1) + f(2-2)

#
# print('我是%s来自%d收入%.2f' % (name, age, money))
# print('{}是我{}{}'.format(name, age, money))

# def area(*args):
#
#     for i in args:
#         res = 4 * math.pi * args**2
#         print('%.2f\n' % res)
#
#
# area(1)

# balls = [1, 2, 4, 9, 10, 13]
# # res = area(balls)
# print(res)
