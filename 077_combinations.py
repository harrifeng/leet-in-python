"""
Given two integers n and k, return all possible combinations of k numbers out
of 1 ... n.
For example,
If n = 4 and k = 2, a solution is:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(sorted([[2, 4],
                                 [3, 4],
                                 [2, 3],
                                 [1, 2],
                                 [1, 3],
                                 [1, 4], ]), sorted(solution.combine(4, 2)))


class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def helper(cur, n, k, tmp, ret):
            if k == 0:
                ret.append(tmp[:])
                return
            for i in range(cur, n + 1):
                tmp.append(i)
                helper(i + 1, n, k - 1, tmp, ret)
                tmp.pop()

        ret = []
        helper(1, n, k, [], ret)
        return ret
