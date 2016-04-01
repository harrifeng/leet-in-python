"""
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
Given n and k, return the kth permutation sequence.
Note: Given n will be between 1 and 9 inclusive.
"""
import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual("213", solution.getPermutation(3, 3))


class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 0:
            return ""

        line = "123456789"

        ret = ""
        group = self.jiecheng(n)

        k -= 1
        for i in reversed(range(1, n + 1)):
            group = group / i
            now = k / group
            k -= now * group
            ret += line[now]
            line = line[:now] + line[now + 1:]

        return ret

    def jiecheng(self, n):
        if n == 1:
            return 1
        ret = 1
        for i in range(1, n + 1):
            ret *= i
        return ret
