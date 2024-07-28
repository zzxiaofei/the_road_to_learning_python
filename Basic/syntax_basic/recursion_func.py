import requests

"""
递归就是函数内在调用这个函数

递归的特性：

1.必须有一个明确的结束条件，要不然就会变成死循环了，最终撑爆系统。
2.每次进入更深一层递归时，问题规模相比上次递归都应有减少。
3.递归执行效率不高，递归层次过多会导致栈溢出。

"""


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(4))  # 输出4的阶乘



