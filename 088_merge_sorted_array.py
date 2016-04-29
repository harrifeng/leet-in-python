"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
sorted array.
Note:
You may assume that nums1 has enough space (size that is greater or equal to m
+ n) to hold additional elements from nums2. The number of elements
initialized in nums1 and nums2 are m and n respectively.
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        nm1 = [1, 3, 5, 0, 0, 0]
        m = 3
        nm2 = [2, 4, 6]
        n = 3
        e1 = [1, 2, 3, 4, 5, 6]
        solution.merge(nm1, m, nm2, n)
        self.assertEqual(e1, nm1)


class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        x = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[x] = nums1[i]
                i -= 1
            else:
                nums1[x] = nums2[j]
                j -= 1
            x -= 1
        while j >= 0:
            nums1[x] = nums2[j]
            x -= 1
            j -= 1
        return