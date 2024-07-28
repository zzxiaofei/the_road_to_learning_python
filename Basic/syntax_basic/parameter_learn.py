import json

"""
非固定参数
1. 元祖形式 *args
如果参数中出现*，传递的参数就不再是个对公的个体了，传过来的所有参数打包成了一个元祖
"""

# def parameter_learn(msg, *users):
#     # for user in users:
#     #     print(f"{user}")
#     print(users)

# parameter_learn("aaa", "alex", "gao", "hong") # 此时的alex、gao、hong都传到了user中

"""
元祖和字典形式
"""

# def func(name, *args, **kwargs):
#     print(name, args, kwargs)
#
#
# func("aa", 1, 2, 3, 4)  # 此时1,2,3,4全部属于args元祖里面打印结果: aa,(1,2,3,4)
# func("aa", 1, 2, 3, age=23,
#      old="bb")  # 此时1,2,3属于args元祖里面，age=23,old="bb"属于kwargs字典里面打印结果: aa,(1,2,3,4){"age"=23,"old"="bb"}
# d = {"degree": "primary school"}
# func("aa", d)  # 此时d这个字典在args元祖里面打印结果:aa,({"degree":"primary school"},)
# func("aa", **d)  # 此时d这个字典在kwargs字典里面打印结果:aa,(),{"degree":"primary school"}


"""
3.关键参数

关键参数定义规则：

1.关键参数不能放在位置参数前面

print("aaa",job="python",21)此时位置参数21放在了job="python"关键参数后面，所以会报错

2.关键参数被定义了一个量以后，不能再被定义第二个量

print("aaa",age=23,21)此时关键参数已经给age赋过值，再赋21会报错


排列顺序：位置参数 关键参数 默认参数
"""


def intro(name, age, job, country="cn"):
    print("-----introduct-------")

    print(name, age, country, job)


intro("aaa", age=23, job="salary")
# intro("aaa", age=23, "job" = "salary")
