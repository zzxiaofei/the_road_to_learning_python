import functools

"""
闭包的概念：在内部可以调用外部函数和这个外部函数所属作用域内的变量值
装饰器：可以让其他函数在不需要任何代码变动的前提下增加额外的功能，装饰器的返回值也是一个函数对象
"""
user_status = False

"""
1.没有加参数的装饰器

思路分析：
第一步会执行login(henan)函数，返回inner的内存地址，此时新henan为inner的内存地址，此时的func为老河南的方法。
第二步执行inner函数，当用户名输入正确时会执行func函数，此时执行老河南的方法，最后输出老河南函数中的内容。
"""
# def login(func):  # 第一次执行login方法时，将老河南的方法保存在了func中
#
#     def inner():  # 装饰器可以随便加多少参数
#         _username = "alex"  # 假装这是DB里存的用户信息
#         _password = "abc!23"  # 假装这是DB里存的用户信息
#         global user_status
#
#         if user_status == False:
#             username = input("user:")
#             password = input("pasword:")
#
#             if username == _username and password == _password:
#                 print("welcome login....")
#                 user_status = True
#             else:
#                 print("wrong username or password!")
#         if user_status:
#             print("用户已登录，验证通过...", func)
#
#             func()  # 此时执行的func为一开始存储的老河南方法
#
#     # print(func)
#     # print(inner)
#     return inner
#
#
# def home():
#     print("---首页----")
#
#
# def america():
#     print("----欧美专区----")
#
#
# def japan():
#     print("----日韩专区----")
#
#
# def henan():
#     print("----河南专区----")
#
#
# henan = login(henan)  # 此时为inner方法的地址
# print(henan)  # 此时为新河南
# henan()  # 为inner


"""
加一个参数的装饰器
当有些函数只要一个参数，有些参数需要多个参数时，inner中的参数为（*args，**kwargs）
"""

Status = False


def login(func):
    def inner(ss):
        name = "gaohui"
        passwd = "1234"
        global Status

        if Status == False:
            username = input("请输入名字:").strip()
            password = input("请输入密码:").strip()

            if username == name and password == passwd:
                # print("欢迎")
                Staus = True
            else:
                print("用户或密码错误")
        if Status:
            print("欢迎")
            func(ss)

    return inner


@login
def henan(style):
    print("欢迎河南")


@login
def Japan(style):
    print("欢迎日本")


def Afica():
    print("欢迎非洲")


henan("3p")
Japan("4p")


"""
当两个参数的时候，再多加一层函数即可实现
"""

user_status = False  # 用户登录了就把这个改成True


def login(auth_type):
    def auth(func):
        def inner(*args, **kwargs):
            _username = "alex"  # 假装这是DB里存的用户信息
            _password = "abc!23"  # 假装这是DB里存的用户信息
            global user_status

            if user_status == False:
                username = input("user:")
                password = input("pasword:")

                if username == _username and password == _password:
                    print("welcome login....")
                    user_status = True
                else:
                    print("wrong username or password!")
            if user_status:
                print("用户已登录，验证通过...", func)

                func(*args, **kwargs)

        return inner

    return auth


def home():
    print("---首页----")


def america():
    print("----欧美专区----")


def japan():
    print("----日韩专区----")


@login('qq')  # henan =  login('qq')(henan)
def henan(video_type):
    print("----河南专区----", video_type)


henan('3p')
