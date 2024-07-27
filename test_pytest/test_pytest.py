import pytest
import requests

"""
定义fixture跟定义普通函数差不多，唯一区别就是在函数上加个装饰器@pytest.fixture()
fixture命名不要以test开头，跟用例区分开。fixture是有返回值，没有返回值默认为None。用例调用fixture的返回值，直接就是把fixture的函数名称当做变量名称。
"""

"""
fixture当作参数传入
"""

# @pytest.fixture()
# def test1():
#     a = 'hello pytest'
#     return a
#
#
# def test2(test1):
#     assert test1 == 'hello pytest'


"""
如果用例需要用到多个fixture的返回数据，fixture也可以返回一个元祖，list或字典，然后从里面取出对应数据。

"""

# @pytest.fixture()
# def test3():
#     a = 'hello pytest'
#     b = '123456'
#     print('传出a,b')
#     return a, b
#
#
# def test4(test3):
#     u = test3[0]
#     p = test3[1]
#     assert u == 'hello pytest'
#     assert p == '123456'
#     print('元祖形式正确')

"""
分成多个fixture，然后在用例中传多个fixture参数
"""

# @pytest.fixture()
# def test1():
#     a = 'leo'
#     print('\n传出a')
#     return a
#
#
# @pytest.fixture()
# def test2():
#     b = '123456'
#     print('传出b')
#     return b
#
#
# def test3(test1, test2):
#     u = test1
#     p = test2
#     assert u == 'leo'
#     assert p == '123456'
#     print('传入多个fixture参数正确')


"""
fixture互相调用
"""

# @pytest.fixture()
# def test1():
#     a = 'leo'
#     print('\n传出a')
#     return a
#
#
# def test2(test1):
#     assert test1 == 'leo'
#     print('fixture传参成功')


# @pytest.fixture()
# def func():
#     print('ready to go')
#
#
# def test_request(func):
#     data_youdao = {
#         "text": "hello"
#     }
#     url = "https://dict.youdao.com/keyword/key"
#     r = requests.post(url, data_youdao)
#
#     assert r.status_code == 200
#     result = r.json()
#     assert result['code'] == 0
#     assert result['message'] == 'SUCCESS'
#     assert result['data'] == []


# def test_two():
#     assert 1 == 1
#     assert 1 != 2
#     assert 1 < 2
#     assert 2 > 1
#     # assert 1 >= 2
#     assert 1 <= 1
#     assert 'a' in 'abc'
#     assert 'a' not in 'bcd'
#     assert True is True
#     assert False is False

# def test_pytest():
#     expect = 1
#     actual = 2
#     assert expect == actual

"""
fixture的作用范围
    :scope: scope参数可以控制fixture的作用范围 session>module>class>function(default)
        :function: 每一个函数或方法都会调用
        :class: 每一个类调用一次，一个类中可以有多个方法
        :module: 每一个.py文件调用一次，该文件有多个function和class
        :session: 是多个文件调用一次，可以跨.py文件调用，每个py文件就是module

fixture源码详解
    :fixture（scope='function'，params=None，autouse=False，ids=None，name=None）
    :scope: 有四个级别参数"function"（默认），"class"，"module"，"session"
    :params: 一个可选的参数列表，它将导致多个参数调用fixture功能和所有测试使用它
    :autouse: 如果True，则为所有测试激活fixture func可以看到它。如果为False则显示需要参考来激活fixture
    :ids:每个字符串id的列表，每个字符串对应于params这样他们就是测试ID的一部分。如果没有提供ID它们将从params自动生成
    :name: fixture的名称。这默认为装饰函数的名称。如果fixture在定义它的统一模块中使用，夹具的功能名称将被请求夹具的功能arg遮蔽，
    解决这个问题的一种方法时将装饰函数命令"fixture_<fixturename>"然后使用"@pytest.fixture（name='<fixturename>'）"。
"""

"""
scope = "function"
@pytest.fixture() 如果不写参数，参数就是scope="function"，它的作用范围是每个测试用例来之前运行一次，销毁代码在测试用例之后运行
"""

#
# @pytest.fixture()
# def test1():
#     a = 'leo'
#     print('\n传出a')
#     return a
#
#
# @pytest.fixture(scope='function')
# def test2():
#     b = '男'
#     print('\n传出b')
#     return b
#
#
# def test3(test1):
#     name = 'leo'
#     print('找到name')
#     assert test1 == name
#
#
# def test4(test2):
#     sex = '男'
#     print('找到sex')
#     assert test2 == sex

"""
fixture scope为class, 如果class里面有多个用例，都调用了次fixture，那么此fixture只在class里所有用例开始前执行一次
"""

# @pytest.fixture(scope='class')
# def test1():
#     b = '男'
#     print('传出了%s, 且只在class里所有用例开始前执行一次！！！' % b)
#     return b
#
#
# class TestCase:
#     def test3(self, test1):
#         name = '男'
#         print('找到name')
#         assert test1 == name
#
#     def test4(self, test1):
#         sex = '男'
#         print('找到sex')
#         assert test1 == sex


"""
fixture为module时，在当前.py脚本里面所有用例开始前只执行一次。
"""


# @pytest.fixture(scope='module')
# def test1():
#     b = '男'
#     print('传出了%s, 且在当前py文件下执行一次！！！' % b)
#     return b
#
#
# def test3(test1):
#     name = '男'
#     print('找到name')
#     assert test1 == name
#
#
# class TestCase:
#
#     def test4(self, test1):
#         sex = '男'
#         print('找到sex')
#         assert test1 == sex


if __name__ == '__main__':
    pytest.main()
