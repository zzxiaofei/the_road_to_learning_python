import math


# import logging
# import time
#
#
# def func_practice(username):
#     print(f"Hello,{username.title()}")
#
#
# def display_message():
#     print('function')
#
#
# def favorite_book(book_name):
#     print("I love " + book_name)
#
#
# def describe_pet(animal_type, pet_name):
#     print(f"I have a {animal_type}")
#     print(f"My {animal_type}'s nam is {pet_name.title()}")
#
#
# # 不定长参数
# def fun1(*args):
#     """
#     不定长函数
#     :param args:
#     :return:
#     """
#     # print(args)
#     # print(type(args))
#     sum_1 = 0
#     for arg in args:
#         sum_1 = sum_1 + arg
#     print(f"The sum of {sum_1}")
#
#
# def fun2(**warg):
#     print(warg)
#     print(type(warg))
#
#
# #
# # fun1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# # fun2(name='name', h='18')
#
# # func_practice('Daniel')
# # display_message()
# # favorite_book('Alice in Wonderland')
# # describe_pet('hamster', 'harry')
# # describe_pet('dog', 'dudu')
#
# # n = 5
# # sum_1 = 1
# # for i in range(1, n + 1):
# #     # print(i)
# #     sum_1 = sum_1 * i
# # print(sum)
#
#
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
#
# # res = fun4(5)
# # print(res)
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

def area(*args):

    for i in args:
        res = 4 * math.pi * args**2
        print('%.2f\n' % res)


area(1)

# balls = [1, 2, 4, 9, 10, 13]
# # res = area(balls)
# print(res)
