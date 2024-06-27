# def x(a, b=1, *c, **d):
#     print(f"a={a}")
#     print(f"b={b}")
#     print(f"c={c}")
#     print(f"d={d}")
#
#
# x(2)
# x(2, 3)
# x(2, 3, 4, 5)
# x(2, 3, 4, 5, x=1, y=2)


class MyClass:
    i = 12345

    def f(self):
        return "hello world"
    x = MyClass()
    x.f()
