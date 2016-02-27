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


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = "^#" + '#'.join(s) + "#$"
        size = [0] * 3000
        i = 1
        tmpc, tmpr, maxp, maxi = 0, 0, 0, 0

        for i in range(1, len(t) - 1):
            if tmpr > i:
                start = min(size[2 * tmpc - i], tmpr - i)
            else:
                start = 1
            while t[i + start] == t[i - start]:
                start += 1
            size[i] = start

            if size[i] + i > tmpr:
                tmpr = size[i] + i
                tmpc = i
            if maxp < size[i]:
                maxp = size[i]
                maxi = i
        return s[maxi / 2 - maxp / 2: maxi / 2 - maxp / 2 + maxp - 1]
