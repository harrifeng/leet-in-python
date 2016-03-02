"""
Implement atoi to convert a string to an integer.
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(123, solution.myAtoi("123"))
        self.assertEqual(-123, solution.myAtoi("-123"))
        self.assertEqual(2147483647, solution.myAtoi("2147483648"))
        self.assertEqual(-2147483648, solution.myAtoi("-2147483648"))
        self.assertEqual(0, solution.myAtoi(""))


class Solution(object):

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        max_int = 2 ** 31 - 1
        min_int = - 2 ** 31
        beg = 0
        while str[beg] == ' ':
            beg += 1
        neg = False
        if str[beg] == '+':
            beg += 1
        if str[beg] == '-':
            beg += 1
            neg = True

        ret = 0
        for i in range(beg, len(str)):
            cur = ord(str[i]) - ord('0')
            if ret > max_int / 10 or ret == max_int/10 and cur > max_int % 10:
                if neg:
                    return min_int
                else:
                    return max_int
            ret = ret * 10 + cur
        if neg:
            return -1 * ret
        else:
            return ret
