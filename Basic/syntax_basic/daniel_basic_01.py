# import keyword
# print(keyword.kwlist)


# 切片
# l = 'learnpythonhappy'  # 正序6-11 python
# print(l[5:12])
# print(l[5:11:1])
# print(l[5:11:2])

# print(l[-11:])  # 反序-11--6获取python

# players = ['charles', 'david', 'john', 'florence', 'eli']
# print(players[-1:0:-1])

# 从右到左,部长为负数
# print(l[-6:-12:-1])  #nohtyp  -6-11

"""布尔值：bool方法"""

#
# n = 10  # True
# a = 0  # False
# s = ''  # False
# m = 'jklj'  # True
# #
# print(bool(n), bool(a), bool(s), bool(m))

# 多个条件判断：与算法and 俩个同时为真才为真，否则为假
#                或运输or,只要有一个为真，结果就为真
#                非运算 not

# print(True and True)
# print(bool(n) and bool(m))
# print(True and False)
# print(False or True)
# print(True or False)
# print(False or False)
# print(not True)
# print(not False)


# # '''字符串常用方法'''
# l = 'learnpythonhappy'
# s = '4302565655454x'
# print(l.startswith('x'))
# print(l.endswith('y'))
# '''判断字符串是否以l开头，以y结尾'''
# print(l.startswith('l') and l.endswith('y'))
# print(s.isdigit())  # 判断一个身份证号码是否包含了字母x

# m = ' fd   sio   jh  jh   '
# print(m)
# print(m.strip('f'))
# print(m.lstrip())  # 去掉左边
# print(m.rstrip())  # 去掉右边空格

# x='###jkljfdsf%%%##'
# print(x.replace('#','%',1)) #替换次数不填，默认替换所有的
# print(m.replace(' ',''))

# print(l.upper())
# print(l.lower())


# msg = 'qingfeng&changsha&18'
# print(msg.split('&'))
# print(msg.split('&', 1))  # 分离次数不填，默认分离所有的

# lst = ['daniel']
# print(type(lst), lst, len(lst))

# lst2 = [100, 'hello', 120.5, True]
# print(lst2)

# print((lst + lst2))
# print(lst2 * 2)
#
# print(lst2[1])
#
# lst2.append('list')
# print(lst2)
# lst2.insert(1, 'list')
# print(lst2)
#
# lst.extend(lst2)
# print(lst)
#
# lst.remove('list')
# print(lst)
#
# new = lst.pop(3)
# print(new)
# print(lst)


# lst.clear()
# print(lst)

# print(lst2)
# del lst2[1:3]
# print(lst2)
#
# lan = ['jan', 'feb', 'mar', 'apr']
# # lan[0] = 'mar'
# # print(lan)
# print(lan[1:3:1])
# lan[1:3:1] = ["May"]
# print(lan)
#
# print(lan.reverse())
# print(lan.count(''))

# tp = ('test', 'test', 'test', 'test')
# # print(id(tp), tp, type(tp))
#
# new_tp = (123, 'tuple_example', True, [1, 2, 3], ('a', 'b', 'c'))
# # print(new_tp)
#
# # print(new_tp[::-1])
#
# # print(new_tp[1][2])
#
# new_tp[3][0] = 4
# print(new_tp)
#
# print(new_tp.index("tuple_example"))
# print(new_tp.__sizeof__())
#
# d1 = {}
# print(id(d1), d1, type(d1))
d2 = {
    "name": "Daniel",
    "phone": "0123456789",
    "email": "<EMAIL>"
}
# print(len(d2))
# print(d2['phone'])
# print(d2.keys())
#
# d2['address'] = 'dalian'
# d2.pop('address')
#
# last = d2.popitem()
# print(last)
# print(d2)

# d2.clear()
# print(d2)


# 字典常用方法

# d3 = {
#     'id': 1001,
#     'name': 'Daniel',
#     'age': 31,
#     'skill': ['python', 'java', 'web'],
#     'hobbies': ['swimming', 'singing'],
#     'address': {'company': 'Beijing', 'base': 'Dalian'}
# }

# .items() 返回可遍历的键、值、元祖数据
# .keys() 返回一个字典所有的key，返回一个迭代器，可以使用list()，来转换成列表
# .values() 返回一个字典所有的值，返回一个迭代器，可以使用list(), 来转换为列表
# .get(key,default)  根据key去字典中获取对应的值，如果key不存在，则返回NONE
# print(d3.items())
# print(d3.keys())
# print(d3.val ues())
# print(d3['hobbies'])
# print(d3.get('age'))


# 集合
# s = set()
# print(id(s), s, type(s))

s1 = {'name', 'phone', 'email'}
# print(id(s1), s1, type(s1))
#
# s1.add(1)
# s1.add('test')
# s1.update([1, 2, 3])
# print(s1)
#
# s1.pop()
# s1.remove('test')
# s1.clear()
# print(s1)

# 集合
s3 = {'s4', 's5', 's6'}
s4 = {'s6', 's7', 's8'}
print(s3 & s4)
print(s3.intersection(s4))

print(s3.union(s4))
print(s3.difference(s4))


