"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.
Your algorithm should run in O(n) time and uses constant space.
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(5, solution.firstMissingPositive(
            [0, 2, 2, 4, 0, 1, 0, 1, 3, 6, 7, 9]))


class Solution:
    # @param A, a list of integers
    # @return an integer

    def firstMissingPositive(self, A):
        N = len(A)
        i = 0
        while i < N:
            if A[i] <= 0 or A[i] == i + 1 or A[i] > N:
                i += 1
            else:
                x = A[i]
                if A[i] == A[x - 1]:
                    i += 1
                    continue
                A[i], A[x - 1] = A[x - 1], A[i]

        for i in range(N):
            if A[i] != i + 1:
                return i + 1

        return N + 1
