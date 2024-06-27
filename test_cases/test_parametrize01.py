import pytest


# # 单参数单词循环
# @pytest.mark.parametrize("key", ["value"])
# def test_parametrize(key):
#     print('I am ' + key)


# 多参数多次循环
@pytest.mark.parametrize("name", ["安琪拉", "黄忠", "大乔"])
def test_parametrize(name):
    assert name == '安琪拉'


