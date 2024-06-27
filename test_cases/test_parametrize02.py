import pytest


# # 单参数单词循环
# @pytest.mark.parametrize("key", ["value"])
# def test_parametrize(key):
#     print('I am ' + key)


# 多参数多次循环
@pytest.mark.parametrize("name, copy", [["安琪拉", "火烧屁屁了"], ["黄忠", '熄火了'], ["鲁班", "上上下下左左右"]])
def test_parametrize02(name, copy):
    # assert name == '安琪拉'
    print(f'{name}的copy是{copy}')
