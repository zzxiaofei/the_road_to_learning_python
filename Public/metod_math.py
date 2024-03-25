import math
import random
#
# # 随机生成一个0-1之间的数字
# math_random = random.random()
# print(math_random)
#
# # 生成一个指定范围内的随机数
# new_math_random = random.random() * 10
# print(new_math_random)
#
# # 直接舍弃小数部分
# nopoints = math.floor(new_math_random)
# print(nopoints)
#
# # 进1法 整数部分+1
# addmore = math.ceil(new_math_random)
# print(addmore)
# newaddmore = math.ceil(8.232323233231121)
# print(newaddmore)
#
# # 随机生成一个小数并对其进行四舍五入
# fourtofive = round(random.random() * 10)
# print("fourtofive:", fourtofive)
#
# # 随机生成一个用户名
# num = ""
# for i in range(3):
#     num += str(random.randint(0, 9))
#     username = "Daniel" + num
# print(username)
#
# for _ in range(100):
#     random_num = str(random.randint(100, 999))
#     username = "Daniel" + random_num
#     print(username)

# 随机生成一个手机号

# lst = ['135', '138', '156', '181', '199']
#
# index = random.randint(0, len(lst) - 1)
#
# pre_phone3 = lst[index]
# print(type(pre_phone3))
# back_phone8 = ""
#
# for i in range(8):
#     back_phone8 += str(random.randint(0, 9))
#
# phonenum = pre_phone3 + back_phone8
#
# print(phonenum)

# 随机生成100个手机号
new_lst = ['135', '138', '156', '181', '199']

for _ in range(100):
    index_New = random.randint(0, len(new_lst) - 1)
    new_pre_phone3 = new_lst[index_New]
    new_back_phone8 = "".join([str(random.randint(0, 9)) for _ in range(8)])
    new_phonenum = new_pre_phone3 + new_back_phone8
    print(new_phonenum)
