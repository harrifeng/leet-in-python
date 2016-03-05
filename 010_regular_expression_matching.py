"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a")  -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "a*") -> true
isMatch("aa", ".*") -> true
isMatch("ab", ".*") -> true
isMatch("aab", "c*a*b") -> true
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertTrue(solution.isMatch("aa", "aa"))
        self.assertTrue(solution.isMatch("aa", "a*"))
        self.assertTrue(solution.isMatch("aa", ".*"))
        self.assertTrue(solution.isMatch("ab", ".*"))
        self.assertTrue(solution.isMatch("aab", "c*a*b"))
        self.assertFalse(solution.isMatch("aa", "a"))
        self.assertFalse(solution.isMatch("aaa", "aa"))


class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0
        if len(p) == 1:
            return len(s) == 1 and (p[0] == '.' or p[0] == s[0])
        if p[1] == '*':
            if self.isMatch(s, p[2:]):
                return True
            else:
                return (len(s) > 0 and (p[0] == '.' or s[0] == p[0]) and
                        self.isMatch(s[1:], p))
        else:
            return (len(s) > 0 and (p[0] == '.' or s[0] == p[0]) and
                    self.isMatch(s[1:], p[1:]))
