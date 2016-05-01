"""
Given n, how many structurally unique BST's (binary search trees) that store
values 1...n?
For example,
Given n = 3, there are a total of 5 unique BST's.
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(14, solution.numTrees(4))
        self.assertEqual(5, solution.numTrees(3))
        self.assertEqual(2, solution.numTrees(2))
        self.assertEqual(1, solution.numTrees(1))


class Solution(object):

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n

        def isValid(arr):
            N = len(arr)
            if N == 0:
                return True
            if arr[0] == 0:
                return sum(arr[1:N]) == 0
            if N == 1:
                return True
            half = N / 2
            for i in range(1, 1 + half):
                if arr[i] != 0 and arr[0] < arr[i]:
                    return False
            for i in range(1 + half, N):
                if arr[i] != 0 and arr[0] > arr[i]:
                    return False
            return isValid(arr[1:half + 1]) and isValid(arr[half + 1:])

        def helper(arr, level, ret):
            if len(arr) == level:
                ret.append(arr[:])
                return

            for i in range(level, len(arr)):
                if i == level or arr[i] not in arr[level:i]:
                    arr[i], arr[level] = arr[level], arr[i]
                    helper(arr, level + 1, ret)
                    arr[i], arr[level] = arr[level], arr[i]
        arr = [0] * (2 ** n - 1)
        for i in range(1, n + 1):
            arr[i] = i
        ret = []
        helper(arr, 0, ret)

        cnt = 0
        for c in ret:
            if isValid(c):
                cnt += 1
        return cnt
