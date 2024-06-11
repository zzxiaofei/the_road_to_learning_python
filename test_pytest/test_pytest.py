# def test_pytest():
#     expect = 1
#     actual = 2
#     assert expect == actual

def test_two():
    assert 1 == 1
    assert 1 != 2
    assert 1 < 2
    assert 2 > 1
    assert 1 >= 2
    assert 1 <= 1

    assert 'a' in 'abc'
    assert 'a' not in 'bcd'
    assert True is True
    assert False is False
