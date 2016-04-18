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

        def helper(nums, k, level, tmp, ret):
            if k == 0:
                ret.append(tmp[:])
                return
            for c in nums[level:]:
                if len(tmp) > 0 and tmp[-1] >= c:
                    continue
                tmp.append(c)
                helper(nums, k - 1, level + 1, tmp, ret)
                tmp.pop()
        ret = []
        nums = []
        for i in range(1, n + 1):
            nums.append(i)
        helper(nums, k, 0, [], ret)
        return ret
