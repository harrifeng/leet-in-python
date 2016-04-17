"""
Given an array with n objects colored red, white or blue, sort them so that
objects of the same color are adjacent, with the colors in the order red,
white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.
Note:
You are not suppose to use the library's sort function for this problem.
"""
import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        r1 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2]
        a1 = [0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 2, 2, 0, 2, 2]
        solution.sortColors(a1)
        self.assertEqual(r1, a1)

        r2 = [2, 2]
        a2 = [2, 2]
        solution.sortColors(a2)
        self.assertEqual(r2, a2)


class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        end = N - 1
        beg = 0

        while beg < end:
            if nums[end] == 2:
                end -= 1
                continue
            if nums[beg] == 0:
                beg += 1
                continue
            if nums[beg] == 1:
                tmp = beg + 1
                while tmp <= end and nums[tmp] == 1:
                    tmp += 1
                if tmp > end:
                    return

                nums[beg], nums[tmp] = nums[tmp], nums[beg]
                continue
            if nums[beg] == 2:
                nums[beg], nums[end] = nums[end], nums[beg]
                end -= 1
        return
