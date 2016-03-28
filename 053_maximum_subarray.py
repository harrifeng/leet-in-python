"""
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.
For example, given the array [-2, 1, -3, 4, -1, 2, 1, -5, 4]
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""
import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(6, solution.maxSubArray(
            [-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(1, solution.maxSubArray([-2, 1]))


class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N == 0:
            return 0

        tmpv, maxv = nums[0], nums[0]
        for i in range(1, N):
            maxv = max(maxv, tmpv)
            if tmpv < 0:
                tmpv = 0
            tmpv += nums[i]

        return max(maxv, tmpv)
