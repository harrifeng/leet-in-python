"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
"""
import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(13, solution.climbStairs(6))


class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        a = 1
        b = 2
        c = a + b
        for i in range(n - 2):
            c = a + b
            a = b
            b = c
        return c
