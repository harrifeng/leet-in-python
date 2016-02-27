"""
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000, and there
exists one unique longest palindromic substring.
For example:
  input: "abccbaaaa"
  output: "abccba"
"""

import unittest


class MyTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual("abccba", solution.longestPalindrome("abccbaaaa"))
        self.assertEqual("cc", solution.longestPalindrome("ccd"))
        self.assertEqual("bb", solution.longestPalindrome("abb"))
        self.assertEqual("a", solution.longestPalindrome("a"))
        self.assertEqual("bcb", solution.longestPalindrome("abcbe"))
        self.assertEqual("aaabaaa", solution.longestPalindrome("aaabaaaa"))


class Solution:
    def longestPalindrome(self, s):
        t = '$#' + '#'.join(s) + '#_'
        p = [0] * 4010
        mx, id, mmax, right = 0, 0, 0, 0
        for i in range(1, len(t) - 1):
            if mx > i:
                p[i] = min(p[2 * id - i], mx - i)
            else:
                p[i] = 1
            while t[i + p[i]] == t[i - p[i]]:
                p[i] += 1
            if i + p[i] > mx:
                mx = i + p[i]
                id = i
            if mmax < p[i]:
                mmax = p[i]
                right = i
        return s[right / 2 - mmax / 2: right / 2 - mmax / 2 + mmax - 1]
