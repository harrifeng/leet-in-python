"""
A message containing letters from A-Z is being encoded to numbers using the
following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of
ways to decode it.
For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
The number of ways decoding "12" is 2.
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(3, solution.numDecodings("123"))
        self.assertEqual(0, solution.numDecodings("00"))
        self.assertEqual(1, solution.numDecodings("10"))
        self.assertEqual(1, solution.numDecodings("20"))
        self.assertEqual(1, solution.numDecodings("27"))
        self.assertEqual(1, solution.numDecodings("1"))
        self.assertEqual(0, solution.numDecodings("100"))
        self.assertEqual(1, solution.numDecodings("101"))
        self.assertEqual(1, solution.numDecodings("110"))
        self.assertEqual(0, solution.numDecodings("301"))
        self.assertEqual(0, solution.numDecodings("01"))
        self.assertEqual(0, solution.numDecodings("230"))


class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        N = len(s)
        if N > 0 and s[0] == '0':
            return 0
        if N <= 1:
            return N
        dp = [1 for i in range(N)]

        # s[0] can not be 1 here
        if int(s[:2]) == 10 or int(s[:2]) == 20:  # half valid
            dp[1] = 1
        elif int(s[:2]) > 10 and int(s[:2]) <= 26:  # full valid
            dp[1] = 2
        elif s[1] == '0':
            dp[1] = 0
        else:
            dp[1] = 1  # non-valid

        for i in range(2, N):
            cnt = 0
            if s[i] == '0':
                # half valid
                if int(s[i - 1:i + 1]) == 10 or int(s[i - 1:i + 1]) == 20:
                    dp[i] = dp[i - 2]
                    continue
                else:
                    return 0
            if int(s[i - 1:i + 1]) > 10 and int(s[i - 1:i + 1]) <= 26:
                cnt = dp[i - 2]
            elif int(s[i - 1:i + 1]) == 0:
                return 0
            else:
                cnt = 0
            dp[i] = dp[i - 1] + cnt
        return dp[N - 1]
