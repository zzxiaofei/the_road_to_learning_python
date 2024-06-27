# from memory_profiler import profile


# 一、for循环作业
# 1：输出99乘法表

# for i in range(1, 10):
#     print(i)
#     for j in range(1, i + 1):
#         print(j)
#         print(f'{j}x{i}={i * j}\t', end='')
#         # print(f'{j}x{i}={i * j}\t', end='')
#     print()


# 2：经典冒泡排序利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序。
# 冒泡排序：小的排前面，大的排后面
# a = [1, 7, 4, 89, 34, 2]
# n = len(a)
# for i in range(n):
#     # print(i)
#     for j in range(n-i-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print(a)


# 3：有1,2,3,4这四个数字，能组成多少个互不相同且无重复数字的三个数？分别是什么？
# 提示：123，321就是符合要求，数字既不相同，而且每个数字的个十百位也不重复；而121,212就不行，因为数字的各位与百位重复
#
# num = [1, 2, 3, 4]
# lst = []
# for a in num:
#     for b in num:
#         for c in num:
#             if a != b and a != c and b != c:
#                 numbers_unique = a * 100 + b * 10 + c
#                 lst.append(numbers_unique)
# print(lst)


# 4：请用嵌套for循环输入如下直角三角形
# *
# **
# ***
# ****
# *****
#
# triangle = '*'
# for i in range(1, 6):
#     print(triangle * i)
#

# 5：请用嵌套for循环输出如下等边三角形（三个边均是5个*）
# *
# * *
# * * *
# * * * *
# * * * * *
#
# height = 5
# for i in range(1, height + 1):
#     for j in range(i):
#         print('*', end=' ')
#     print()

# 四、for..range练习：
#
# 1：利用for循环和range找出 0 ~ 100 以内所有的偶数，并追加到一个列表。

even_number = []

for i in range(101):
    if i % 2 == 0:
        even_number.append(i)
print(even_number)

#
# 2：利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并追加到一个列表。

lst3 = []
for i in range(51):
    if i % 3 == 0:
        lst3.append(i)
print(lst3)

# 3：利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并插入到列表的第0个索引位置，

lst4 = []
for i in range(51):
    if i % 3 == 0:
        lst4.insert(0, i)
print(lst4)

# 最终结果如下：
# [48,45,42...]
#
# 4：查找列表li中的元素，移除每个元素前后的空格，并找出以”a”开头的元素，添加到一个新列表中,
# 最后循环打印这个新列表。
li = ["alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]

new_li = []
# ln_n = len(li)

for element in li:
    cleaned_li = element.strip()
    if element.lower().startswith('a'):
        new_li.append(cleaned_li)
print(new_li)
