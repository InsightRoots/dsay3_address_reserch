# タイトル、テストのやり方を覚えよう！↑テスト駆動開発（TDP）
# Green→エラーが出ない。つまり、Trueの状態で、この状態を作って、足元というか武器を固めて関数を作っていく。


import unittest


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def kake(x, y):
    return x * y


def wari(x, y):
    return x / y


class MyTestCase(unittest.TestCase):
    #     # 2つの整数の和を計算できるメソッドをためにしにやっている。
    def test_2つの整数の和が計算できる(self):
        self.assertEqual(7, add(3, 4))  # add assertion here

    def test_2つの整数の差が計算できる(self):
        self.assertEqual(-1, sub(3, 4))  # add assertion here

    def test_2つの整数の積が計算できる(self):
        self.assertEqual(12, kake(3, 4))  # add assertion here

    def test_2つの整数の除が計算できる(self):
        self.assertEqual(3, wari(12, 4))  # add assertion here


if __name__ == '__main__':
    unittest.main()
