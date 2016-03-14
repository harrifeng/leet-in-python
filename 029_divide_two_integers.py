"""
Divide two integers without using multiplication, division and mod operator.
If it is overflow, return MAX_INT.
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(5, solution.divide(15, 3))
        self.assertEqual(5000, solution.divide(15000, 3))


class Solution(object):

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend < 0) != (divisor < 0):
            sign = -1
        else:
            sign = 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        ret = 0
        while dividend >= divisor:
            tmp = divisor
            i = 0
            while dividend >= tmp:
                dividend -= tmp
                ret += (1 << i)
                i += 1
                tmp = (tmp << 1)

        imin, imax = -2 ** 31, 2 ** 31 - 1
        if ret * sign > imax:
            return imax
        if ret * sign < imin:
            return imin
        return ret * sign
