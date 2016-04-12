"""
Given an absolute path for a file (Unix-style), simplify it.
For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
"""
import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual("/home", solution.simplifyPath("/home/"))
        self.assertEqual("/c", solution.simplifyPath("/a/./b/../../c/"))


class Solution(object):

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        sta = []

        line = path.split('/')

        for c in line:
            if c == '.':
                pass
            elif c == '..':
                sta.pop()
            else:
                sta.append(c)

        if len(sta) > 1 and sta[-1] == '':
            sta.pop()
        return '/'.join(sta)
