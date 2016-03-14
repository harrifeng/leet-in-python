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

    def strStr(self, s, p):
        """
        :type t: str
        :type p: str
        :rtype: int
        """
        N = len(s)
        M = len(p)
        i, j = 0, 0
        while i < N and j < M:
            if s[i] == p[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0
        if j == M:
            return i - j
        else:
            return -1
