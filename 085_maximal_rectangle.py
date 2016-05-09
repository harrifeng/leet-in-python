"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
containing all ones and return its area.
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(6, solution.maximalRectangle(
            [['0', '0', '0', '0'],
             ['1', '1', '1', '1'],
             ['1', '1', '1', '0'],
             ['0', '1', '0', '0']]
        ))


class Solution(object):

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        h = [0] * (n + 1)
        maxv = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    h[j] = 0
                else:
                    h[j] += 1
            sta = []
            k = 0
            while k < len(h):
                if len(sta) == 0 or h[k] >= h[sta[-1]]:
                    sta.append(k)
                    k += 1
                else:
                    height = h[sta.pop()]
                    if len(sta) == 0:
                        width = k
                    else:
                        width = k - sta[-1] - 1
                    maxv = max(maxv, width * height)
        return maxv
