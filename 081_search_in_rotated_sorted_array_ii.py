"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?
Would this affect the run-time complexity? How and why?
Write a function to determine if a given target is in the array.
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertTrue(solution.search([1, 3, 1, 1, 1], 3))


class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        N = len(nums)
        if N == 0:
            return False

        beg = 0
        end = N - 1

        while beg <= end:
            mid = (beg + end) / 2
            if nums[mid] == target:
                return True
            elif nums[beg] < nums[mid]:  # First half sorted
                if nums[beg] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    beg = mid + 1
            elif nums[beg] > nums[mid]:  # Second half sorted
                if nums[mid] < target and target <= nums[end]:
                    beg = mid + 1
                else:
                    end = mid - 1
            else:
                beg += 1
        return False
