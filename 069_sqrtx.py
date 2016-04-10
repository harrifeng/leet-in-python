"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""
import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(11, solution.mySqrt(121))


class Solution(object):

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0                         # Here must 0, otherwise 1 won't pass
        right = x                        # Use x/2 + 1
        while left <= right:             # <=
            mid = (left + right) / 2
            sqr = mid * mid
            if sqr == x:
                return mid
            elif sqr < x:
                left = mid + 1
            else:
                right = mid - 1
        return (left + right) / 2           # This is so important
