"""
Given a string containing only digits, restore it by returning all possible
valid IP address combinations.
For example:
Given "25525511135",
return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(sorted(["255.255.11.135", "255.255.111.35"]),
                         sorted(solution.restoreIpAddresses("25525511135")))
        self.assertEqual(sorted(["0.10.0.10", "0.100.1.0"]),
                         sorted(solution.restoreIpAddresses("010010")))


class Solution(object):

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def validNPart(s, n, tmp, ret):
            if n == 0:
                if len(s) == 0:
                    ret.append('.'.join(tmp[:]))
                return

            for i in range(1, min(4, len(s) + 1)):
                if int(s[:i]) < 256:
                    if len(s[:i]) > 1 and s[0] == '0':
                        continue
                    tmp.append(s[:i])
                    validNPart(s[i:], n - 1, tmp, ret)
                    tmp.pop()
        ret = []
        validNPart(s, 4, [], ret)
        return ret
