"""
Divide two integers without using multiplication, division and mod operator.
If it is overflow, return MAX_INT.
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(5, solution.divide(15, 3))


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        cnt = 0
        while dividend >= divisor:
            dividend -= divisor
            cnt += 1
        return cnt
