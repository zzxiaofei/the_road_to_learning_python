#!/usr/bin/python3
import hashlib
import random
# @Time : 2023/10/1 18:57
# @Author : Daniel Zhang
# import requests;

# 获得随机字符串


def random_str(digits=True, lowercase=True, uppercase=True, symbol=True, chinese=True, slen=10):

    seed = ''
    seed = seed + '1234567890' if digits else seed + ''
    seed = seed + 'abcdefghijklmopqrstuvwxyz' if lowercase else seed + ''
    seed = seed + 'ABCDEFGHIJKLMOPQRSTUVWXYZ' if uppercase else seed + ''
    seed = seed + '!@#$%^&*()_+=' if symbol else seed + ''
    seed = seed + '你可以的' if chinese else seed + ''

    if len(seed) == 0:
        return None
    sa = []
    for i in range(slen):
        sa.append(random.choice(seed))
    return ''.join(sa)


x = random_str()
print(x)


# MD5加密


def to_md5(params):
    params_str = str(params)
    md5 = hashlib.md5()
    # 生成MD5对象
    md5.update(params_str.encode(encoding='utf-8'))
    # 对数据加密
    params_md5 = md5.hexdigest()
    return params_md5


data = 'Hello, Python'
encrypted_data = to_md5(data)
print("MD5加密结果：", encrypted_data)


# if __name__ == '__main__':
#
#     m = to_md5('channel123456')
#     if m:
#         print('加密成功：', m)
#     else:
#         print('加密失败！')
