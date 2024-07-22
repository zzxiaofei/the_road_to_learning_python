import random
from collections import deque




# # 变量，在使用前都必须赋值，变量赋值以后该变量才会被创建
#
# # 字符串
#
# # x = 'a'
# # y = 'BCD'
# # print(x + y)
# # print(x + " " + y)
# # print(f"{x} {y}")
# # print("{} {} ".format(x, y))
# # print("{m} {n}".format(m=x, n=y))
# # print(y.split('C'))
#
# # 转义字符
# # str_char = '字符串\n中\r可以穿插\t转义字符，\b'
# # '''
# # 转义符号是对应ascii码表的
# # \n 全拼newline的首字母表示换行
# # \t -->tab的首字母表示制表符
# # \r -->return的首字母表示返回
# # \b -->backspace的首字母表示退一个格
# # '字符串\n【换行】中\r【回车】可以穿插\t【制表符，大空格】转义字符，\b【退格，不显示，】'
# # '''
# # print(str_char)
# #
# # str_char = r'字符串\n中\r可以穿插\t转义字符，\b'  # 取消转义字符
#
# # print
#
#
# # 1.if判断语句
# # format： if 条件语句: 符合条件  -  elif 条件语句: 符合条件  -  else: 不符合条件
#
# # x = "zhangxiaofei"
# # if x == "I cant do it":
# #     print("you fucked up")
# # elif x == "犹犹豫豫":
# #     print("It‘s getting later")
# # elif x == "zhangxiaofei":
# #     print("you will do it")
# # else:
# #     print("GO TO HELL")
# #
# # # 练习
# # age = int(input("How old are you? "))
# #
# # if age >= 18:
# #     print("You are allowed to go to bar")
# # else:
# #     print("You are not allowed!")
#
#
# # 2.for 循环语句
# # format： for 条件语句: - else:不符合条件
#
# # 1.循环遍历
# # sum_int = 0
# # for x in range(101):
# #     sum_int = sum_int + x
# # print(sum_int)
# #
# # # 2. 多元素数据  -数组遍历
# # nums = ['one', 'two', 'three']
# # for num in nums:
# #     print(num)
# #
# # # 3. 循环嵌套
# # for i in range(1, 10):
# #     for j in range(1, i + 1):
# #         print(f'{j}x{i}={i * j}\t', end='')
# #     print()
#
# # 4. break & continue
#
# # 5. while
# # 四要素 1.初始值 (i=0) 2. 表达式 (i<10) 3. 循环体 print(i) 4. 迭代器 (i=i+1)
#
"""
字符串
"""

"""
列表:
"""
items1 = [24, 25, 26, 30, 50, 66]
items2 = [45, 6, 7]

# 列表的成员运算
# print(24 in items1)
# print('30' in items2)

# 获取列表的长度（元素个数）
# size = len(items1)
# print(size)

# 列表的索引
# print(items1[0], items1[-size])
# items1[-1] = 100
# print(items1[size - 1], items1[-1])


# # 列表的切片
items3 = [1, 2, 3, 4, 5]
print(items3[1:3])
print(items3[:5])
print(items3[4:])
print(items3[-5:-7:-1])
print(max(items3))
print(min(items3))
# #
# # print(items3.sort())  # sort方法是返回一个None值，虽然没有返回值但它更改了对象自身，且对列表内的数据进行了排序
# #
# # print(items3)
# #
# # items3.append(9)
# # print(items3)
# # print(items3.pop())
# # print(items3)
# #
# # number_queue = deque(items3)
# # number_queue.append("m")
# # number_queue.append("n")
# # print(number_queue)
# # print(number_queue.popleft())
# # print(number_queue)
# #
# # number_list = [x for x in range(10)]
# # print(number_list)
#
# #
# # # 列表的比较运算
# #
# # items5 = [1, 2, 3, 4]
# # items6 = list(range(1, 5))
# #
# # # 两个列表比较相等性比的是对应索引位置上的元素是否相等
# # print(items5 == items6)
# #
# # items7 = [3, 2, 1]
# #
# # # 两个列表比较大小比的是对应索引位置上的元素大小
# # print(items5 <= items7)
# #
# # items = ['Python', 'Java', 'Go', 'Kotlin']
# # for index in range(len(items)):
# #     print(items[index])
# #
# # for item in items:
# #     print(item)
# #
# # counters = [0] * 6
# # for _ in range(6000):
# #     face = random.randint(1,6)
# #     counters[face - 1] += 1
# # for face in range(1,7):
# #     print(f'{face}点出现了{counters[face - 1]}次')
# #
# # items.append('Swift')
# # print(items)
# # items.insert(2, 'SQL')
# # print(items)
# #
# #
# # items.remove('Java')
# # print(items)
# # items.pop(0)
# # items.pop(len(items)-1)
# # print(items)
# #
# # items.clear()
# # print(items)
#
# # items = ['Python', 'Java', 'Go', 'Kotlin']
# # del items[1]
# # print(items)    # ['Python', 'Go', 'Kotlin']
# #
# # items = ['Python', 'Java', 'Java', 'Go', 'Kotlin', 'Python']
# #
# # print(items.index('Python'))
# # print(items.index('Python', 2))
# # print(items.index('Java', 3))
#
#
# # items = ['Python', 'Java', 'Java', 'Go', 'Kotlin', 'Python']
# # print(items.count('Python'))
# #
# # items.sort()
# # print(items)
# # items.reverse()
# # print(items)
# #
# # items1 = []
# # for x in range(1,10):
# #     items1.append(x)
# # print(items1)
# #
# # items2 = []
# # for x in 'hello world':
# #     if x not in ' aeiou':
# #         items2.append(x)
# # print(items2)
# #
# # items3 = []
# # for x in 'ABC':
# #     for y in '12':
# #         items3.append(x + y)
# # print(items3)
# #
# # items1 = [x for x in range(1, 10)]
# # print(items1)
# #
# # items2 = [x for x in 'hello world' if x not in ' aeiou']
# # print(items2)
# #
# # items3 = [x + y for x in 'ABC' for y in '12']
# # print(items3)
# #
# #
# # scores = [[0] * 3 for _ in range(5)]
# # scores[0][0] =95
# # print(scores)
# #
# #
# # t1 = (30, 10, 55)
# # t2 = ('Daniel', 30, True, '辽宁大连')
# # print(type(t1), type(t2))
# # print(len(t1), len(t2))
# #
# # print(t1[0], t1[0])
# # print(t2[3], t2[-1])
# #
# # for member in t2:
# #     print(member)
# #
# # print(100 in t1)
# # print(30 in t2)
# #
# # t3 = t1 + t2
# # print(t3)
# #
# # # 切片
# # print(t3[::3])
# #
# #
# # a = ()
# # print(type(a))
# # b = ('hello')
# # print(type(b))
# # c = (100)
# # print(type(c))
# # d = ('hello', )
# # f = (100, )
# # print(type(d), type(f))
# #
# # a = 1, 10, 100
# # print(type(a), a)
# #
# # i, j, k = a
# # print(i, j, k)
# #
# #
# # a = 1, 10, 100, 1000
# # i, j, *k = a
# # print(i, j, k)
#
#


"""
集合Set，是无序的数据结构
"""
# # number_set = set()
# # number_set.add('m')
# # number_set.add('abc')
# # number_set.add('bcd')
# # number_set.add('efg')
# # number_set.add('bcd')
# # number_set.clear()
# # number_set.update()
# # number_set.remove()
# # print(number_set)
#
# s3 = {'s4', 's5', 's6'}
# s4 = {'s6', 's7', 's8'}
# print(s3 & s4)
# print(s3.intersection(s4))  # 返回两个集合的交集作为新集合
#
# print(s3.union(s4))  # 将两个集合组合成一个新集合
# print(s3.difference(s4))  # 将两个集合的不同组成一个新集合
#
#
#
#
# """
# 元祖 Tuple
# """
#
# # element_tuple = (1, 2, 3, 4, 5)
# # print(element_tuple[1])
#
# # 遍历元祖
# # for element in element_tuple:
# #     print(element)
#
# """
# # 字典dict:
# #
# # .items() 遍历字典，返回一个包含键值对的视图对象
# """
# # my_dict = {'name': 'John', 'age': 23, 'city': 'New York'}
# # for key, value in my_dict.items():
# #     print(f'Key: {key}, Value:{value}')
# #
# # element_dict = {'a': 1, 'b': 2, 'c': 3}
# # print((type(element_dict)))
# # print(type(element_dict))
# # element_dict['mn'] = 'mmmm'
# # print(element_dict)
# # print(element_dict.items())
# # print(element_dict['a'])
# # print(element_dict.keys())
# # print(element_dict.values())
#
# """
# enumerate():可以用于带索引地遍历序列类型（如列表、元组等）
# """
#
# # my_list = ['a', 'b', 'c']
# # for index, item in enumerate(my_list):
# #     print(index, item)
#
# """
# zip:用于并行遍历多个可迭代对象。
# """
#
# # list1 = [1, 2, 3]
# # list2 = ['a', 'b', 'c']
# #
# # for num, char in zip(list1, list2):
# #     print(f"Number: {num}, Character: {char}")
#
#
# bytes_array = bytearray(b"Hello")
# print(type(bytes_array))  # <class 'bytearray'>
#
# range_ = range(5)
# print(type(range_))  # <class 'range'>
#
#
#
# # import keyword
# # print(keyword.kwlist)
#
#
# # 切片
# # l = 'learnpythonhappy'  # 正序6-11 python
# # print(l[5:12])
# # print(l[5:11:1])
# # print(l[5:11:2])
#
# # print(l[-11:])  # 反序-11--6获取python
#
# # players = ['charles', 'david', 'john', 'florence', 'eli']
# # print(players[-1:0:-1])
#
# # 从右到左,部长为负数
# # print(l[-6:-12:-1])  #nohtyp  -6-11
#
# """布尔值：bool方法"""
#
# #
# # n = 10  # True
# # a = 0  # False
# # s = ''  # False
# # m = 'jklj'  # True
# # #
# # print(bool(n), bool(a), bool(s), bool(m))
#
# # 多个条件判断：与算法and 俩个同时为真才为真，否则为假
# #                或运输or,只要有一个为真，结果就为真
# #                非运算 not
#
# # print(True and True)
# # print(bool(n) and bool(m))
# # print(True and False)
# # print(False or True)
# # print(True or False)
# # print(False or False)
# # print(not True)
# # print(not False)
#
#
# # # '''字符串常用方法'''
# # l = 'learnpythonhappy'
# # s = '4302565655454x'
# # print(l.startswith('x'))
# # print(l.endswith('y'))
# # '''判断字符串是否以l开头，以y结尾'''
# # print(l.startswith('l') and l.endswith('y'))
# # print(s.isdigit())  # 判断一个身份证号码是否包含了字母x
#
# # m = ' fd   sio   jh  jh   '
# # print(m)
# # print(m.strip('f'))
# # print(m.lstrip())  # 去掉左边
# # print(m.rstrip())  # 去掉右边空格
#
# # x='###jkljfdsf%%%##'
# # print(x.replace('#','%',1)) #替换次数不填，默认替换所有的
# # print(m.replace(' ',''))
#
# # print(l.upper())
# # print(l.lower())
#
#
# # msg = 'qingfeng&changsha&18'
# # print(msg.split('&'))
# # print(msg.split('&', 1))  # 分离次数不填，默认分离所有的
#
# # lst = ['daniel']
# # print(type(lst), lst, len(lst))
#
# # lst2 = [100, 'hello', 120.5, True]
# # print(lst2)
#
# # print((lst + lst2))
# # print(lst2 * 2)
# #
# # print(lst2[1])
# #
# # lst2.append('list')
# # print(lst2)
# # lst2.insert(1, 'list')
# # print(lst2)
# #
# # lst.extend(lst2)
# # print(lst)
# #
# # lst.remove('list')
# # print(lst)
# #
# # new = lst.pop(3)
# # print(new)
# # print(lst)
#
#
# # lst.clear()
# # print(lst)
#
# # print(lst2)
# # del lst2[1:3]
# # print(lst2)
# #
# # lan = ['jan', 'feb', 'mar', 'apr']
# # # lan[0] = 'mar'
# # # print(lan)
# # print(lan[1:3:1])
# # lan[1:3:1] = ["May"]
# # print(lan)
# #
# # print(lan.reverse())
# # print(lan.count(''))
#
# # tp = ('test', 'test', 'test', 'test')
# # # print(id(tp), tp, type(tp))
# #
# # new_tp = (123, 'tuple_example', True, [1, 2, 3], ('a', 'b', 'c'))
# # # print(new_tp)
# #
# # # print(new_tp[::-1])
# #
# # # print(new_tp[1][2])
# #
# # new_tp[3][0] = 4
# # print(new_tp)
# #
# # print(new_tp.index("tuple_example"))
# # print(new_tp.__sizeof__())
# #
# # d1 = {}
# # print(id(d1), d1, type(d1))
# d2 = {
#     "name": "Daniel",
#     "phone": "0123456789",
#     "email": "<EMAIL>"
# }
# # print(len(d2))
# # print(d2['phone'])
# # print(d2.keys())
# #
# # d2['address'] = 'dalian'
# # d2.pop('address')
# #
# # last = d2.popitem()
# # print(last)
# # print(d2)
#
# # d2.clear()
# # print(d2)
#
#
# # 字典常用方法
#
# # d3 = {
# #     'id': 1001,
# #     'name': 'Daniel',
# #     'age': 31,
# #     'skill': ['python', 'java', 'web'],
# #     'hobbies': ['swimming', 'singing'],
# #     'address': {'company': 'Beijing', 'base': 'Dalian'}
# # }
#
# # .items() 返回可遍历的键、值、元祖数据
# # .keys() 返回一个字典所有的key，返回一个迭代器，可以使用list()，来转换成列表
# # .values() 返回一个字典所有的值，返回一个迭代器，可以使用list(), 来转换为列表
# # .get(key,default)  根据key去字典中获取对应的值，如果key不存在，则返回NONE
# # print(d3.items())
# # print(d3.keys())
# # print(d3.val ues())
# # print(d3['hobbies'])
# # print(d3.get('age'))
#
#


square = [x**2 for x in range(10)]
print(square)
