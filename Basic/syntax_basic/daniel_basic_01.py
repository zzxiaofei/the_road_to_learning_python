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


