"""
Given an array of non-negative integers, you are initially positioned at the
first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
For example:
Given array A = [2,3,1,1,4]
The minimum number of jumps to reach the last index is 2. (Jump 1 step from
index 0 to 1, then 3 steps to the last index.)
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        # self.assertEqual(2, solution.jump([2, 3, 1, 1, 4]))
        self.assertEqual(2, solution.jump_dp([2, 3, 1, 1, 4]))


class Solution(object):

    def jump_dp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        dp = [N for i in range(N)]
        dp[0] = 0
        for i in range(N):
            for j in range(i)[::-1]:
                if nums[j] + j >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[N - 1]
