import pytest
import requests


@pytest.fixture()
def func():
    print("ready to go")


def test_request(func):
    data_youdao = {
        "text": "hello"
    }
    url = "https://dict.youdao.com/keyword/key"
    r = requests.post(url, data_youdao)

    assert r.status_code == 200
    result = r.json()
    assert result['code'] == 0
    assert result['message'] == 'SUCCESS'
    assert result['data'] == []


if __name__ == '__main__':
    pytest.main()
