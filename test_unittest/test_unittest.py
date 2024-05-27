import unittest


def sum_numbers(a, b):
    return a + b


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    def setUp(self) -> None:
        print("setUp")

    def test_sum_numbers_int(self):
        self.assertEqual(sum_numbers(1, 2), 3)
        self.assertEqual(sum_numbers(100, 200), 300)

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(1.1, 2.2), 3.3)


if __name__ == '__main__':
    unittest.main()
