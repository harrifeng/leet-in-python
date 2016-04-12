"""
Validate if a given string is numeric.
Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should
gather all requirements up front before implementing one.
"""
import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertTrue(solution.isNumber("0"))
        self.assertTrue(solution.isNumber(" 0.1 "))
        self.assertFalse(solution.isNumber("abc"))
        self.assertFalse(solution.isNumber("1 a"))
        self.assertTrue(solution.isNumber("2e10"))


class Solution:
    # @param s, a string
    # @return a boolean
    # @finite automation

    def isNumber(self, s):
        s = s.strip()
        s += '#'
        i = 0
        n1, n2, n3 = 0, 0, 0
        if s[i] in ['+', '-']:
            i += 1
        while s[i].isdigit():
            n1 += 1
            i += 1
        if s[i] == '.':
            i += 1

        while s[i].isdigit():
            n2 += 1
            i += 1
        if n1 == n2 == 0:       # e has something on left
            return False
        if s[i] in ['e', 'E']:
            i += 1
            if s[i] in ('+', '-'):
                i += 1
            n3 = 0
            while s[i].isdigit():
                n3 += 1
                i += 1
            if n3 == 0:
                return False    # e has something on right
        return s[i:] == '#'
