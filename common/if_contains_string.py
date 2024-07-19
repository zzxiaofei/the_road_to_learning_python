"""
封装一些公共的方法
"""


def if_contains_string(expected, actual):
    """
    判断字典是否包含一个字符串

    """
    if isinstance(expected, int):
        expected = str(expected)
        # print(expected)
    for key, value in actual.items():
        print(key, value)
        """ 1.预期是字符串，实际结果的value是字符串"""
        if isinstance(value, str):
            if expected in key or expected in value:
                return True
        """ 2.预期是字符串，实际结果的value是整数"""
        if isinstance(value, int):
            value = str(value)
            if expected in key or expected in value:
                return True
        if isinstance(value, dict):
            print(value)
            if expected in key:
                # print(key)
                return True
            print(expected)
            print(value)
            res = if_contains_string(expected, value)
            print(type(res))
            if res is True:
                return True
        if isinstance(value, list):
            for item in value:
                if expected in key:
                    return True
                res = if_contains_string(expected, item)
                if res is True:
                    return True
    return False


if __name__ == '__main__':
    expected_result = 'age'
    # print(type(expected_result))
    actual_result = {
        "adress": {
            "city": "changsha",
        },
        "httpstatus": 200,
        "info": {
            "age": 18,
            "name": "admin"
        },
        "msg": "success",
        "token": "qingfengtest",
        "data": [
            {
                "idqingfeng": 'id1'
            },
            {
                "id": 'id2'
            }
        ]
    }

    print(if_contains_string(expected_result, actual_result))
