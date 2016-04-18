"""
Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in complexity O(n).
For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".
Note:
If there is no such window in S that covers all characters in T, return the
empty string "".
If there are multiple such windows, you are guaranteed that there will always
be only one unique minimum window in S.
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual("BANC", solution.minWindow("ADOBECODEBANC", "ABC"))


class Solution(object):

    def minWindow(self, S, T):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        N = len(S)
        M = len(T)
        wanted = {}
        found = {}
        for char in T:
            wanted[char] = wanted.get(char, 0) + 1
            found[char] = 0
        l = 0
        res = ''
        counter = 0
        for r in range(N):
            if S[r] not in wanted:
                continue

            found[S[r]] += 1
            if found[S[r]] <= wanted[S[r]]:
                counter += 1

            if counter == M:
                while l < r:
                    if S[l] not in wanted:
                        l += 1
                        continue
                    if found[S[l]] > wanted[S[l]]:
                        found[S[l]] -= 1
                        l += 1
                        continue
                    break
                if not res or len(res) > r - l + 1:
                    res = S[l:r + 1]
        return res
