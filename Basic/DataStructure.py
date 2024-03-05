# #!/usr/bin/python3
#
# # @Time : 2023/8/20 15:41
# # @Author : Daniel Zhang
# import random
#
# items1 = [24, 25, 26, 30, 50, 66]
# items2 = [45, 6, 7]
#
# # 列表的拼接
# items3 = items1 + items2
# print(items3)
#
# # 列表的重复
# items4 = ['hello'] * 3
# print(items4)
#
# # 列表的成员运算
# print(100 in items3)
# print('hello' in items4)
#
# # 获取列表的长度（元素个数）
# size = len(items3)
# print(size)
#
# # 列表的索引
# print(items3[0], items3[-size])
# items3[-1] = 100
# print(items3[size - 1], items3[-1])
#
#
# # 列表的切片  ?????
#
# print(items3[:5])
# print(items3[4:])
# print(items3[-5:-7:-1])
#
# # 列表的比较运算
#
# items5 = [1, 2, 3, 4]
# items6 = list(range(1, 5))
#
# # 两个列表比较相等性比的是对应索引位置上的元素是否相等
# print(items5 == items6)
#
# items7 = [3, 2, 1]
#
# # 两个列表比较大小比的是对应索引位置上的元素大小
# print(items5 <= items7)
#
# items = ['Python', 'Java', 'Go', 'Kotlin']
# for index in range(len(items)):
#     print(items[index])
#
# for item in items:
#     print(item)
#
# counters = [0] * 6
# for _ in range(6000):
#     face = random.randint(1,6)
#     counters[face - 1] += 1
# for face in range(1,7):
#     print(f'{face}点出现了{counters[face - 1]}次')
#
# items.append('Swift')
# print(items)
# items.insert(2, 'SQL')
# print(items)
#
#
# items.remove('Java')
# print(items)
# items.pop(0)
# items.pop(len(items)-1)
# print(items)
#
# items.clear()
# print(items)

# items = ['Python', 'Java', 'Go', 'Kotlin']
# del items[1]
# print(items)    # ['Python', 'Go', 'Kotlin']
#
# items = ['Python', 'Java', 'Java', 'Go', 'Kotlin', 'Python']
#
# print(items.index('Python'))
# print(items.index('Python', 2))
# print(items.index('Java', 3))


items = ['Python', 'Java', 'Java', 'Go', 'Kotlin', 'Python']
print(items.count('Python'))

items.sort()
print(items)
items.reverse()
print(items)

items1 = []
for x in range(1,10):
    items1.append(x)
print(items1)

items2 = []
for x in 'hello world':
    if x not in ' aeiou':
        items2.append(x)
print(items2)

items3 = []
for x in 'ABC':
    for y in '12':
        items3.append(x + y)
print(items3)

items1 = [x for x in range(1, 10)]
print(items1)

items2 = [x for x in 'hello world' if x not in ' aeiou']
print(items2)

items3 = [x + y for x in 'ABC' for y in '12']
print(items3)


scores = [[0] * 3 for _ in range(5)]
scores[0][0] =95
print(scores)


t1 = (30, 10, 55)
t2 = ('Daniel', 30, True, '辽宁大连')
print(type(t1), type(t2))
print(len(t1), len(t2))

print(t1[0], t1[0])
print(t2[3], t2[-1])

for member in t2:
    print(member)

print(100 in t1)
print(30 in t2)

t3 = t1 + t2
print(t3)

# 切片
print(t3[::3])


a = ()
print(type(a))
b = ('hello')
print(type(b))
c = (100)
print(type(c))
d = ('hello', )
f = (100, )
print(type(d), type(f))

a = 1, 10, 100
print(type(a), a)

i, j, k = a
print(i, j, k)


a = 1, 10, 100, 1000
i, j, *k = a
print(i, j, k)
