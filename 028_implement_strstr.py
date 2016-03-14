"""
Implement strStr().
Returns the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(3, solution.strStr("abcxyz", "xyz"))
        self.assertEqual(0, solution.strStr("abcde", "abc"))
        self.assertEqual(-1, solution.strStr("abcde", "cdew"))
        self.assertEqual(4, solution.strStr("mississippi", "issip"))


class Solution(object):

    def strStr(self, t, p):
        """
        :type t: str
        :type p: str
        :rtype: int
        """
        N = len(t)
        M = len(p)
        if M == 0:
            return 0
        next = self.pre(p)
        i, k = -1, -1
        while i < N:
            if k == -1 or t[i] == p[k]:
                k += 1
                i += 1
                if k == M:
                    return i - M
            else:
                k = next[k]
        return -1

    def pre(self, p):
        N = len(p)
        next = [-1] * N
        i, k = 0, -1
        while i < N - 1:
            if k == -1 or p[k] == p[i]:
                i += 1
                k += 1
                next[i] = k
            else:
                k = next[k]
        return next
