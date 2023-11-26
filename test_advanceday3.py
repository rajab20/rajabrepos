import unittest
from advanceday3 import add, multiply, is_even, find_max


class Testing(unittest.TestCase):
    # eShoper
    def test_add_pos(self):
        test1 = add(3, 5)
        self.assertEqual(test1, 8)

    def test_add_neg(self):
        test2 = add(-5, -6)
        self.assertEqual(test2, -11)

    # 2
    def test_multiply_pos(self):
        test3 = multiply(8, 88)
        self.assertEqual(test3, 704)

    def test_multiply_neg(self):
        test4 = multiply(-54, 6)
        self.assertEqual(test4, -324)

    # 3
    def test_is_even(self):
        test5 = is_even(56)
        self.assertEqual(test5, True)

    def test_is_odd(self):
        test6 = is_even(37)
        self.assertEqual(test6, False)

    # 4

    def test_find_max_pos(self):
        test7 = find_max([3, 6, 8, 14, 16, 20])
        self.assertEqual(test7, 20)

    def test_find_max_neg(self):
        test8 = find_max([-2, -5, -7, -16, -19, -23])
        self.assertEqual(test8, -2)

    def test_find_max_repeated(self):
        test9 = find_max([-3, 6, 7, 33, -3, 33])
        self.assertEqual(test9, 33)


if __name__ == '__main__':
    unittest.main()
