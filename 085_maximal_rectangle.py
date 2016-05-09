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
        def getH(matrix, i, j):
            if i == 0:
                return 0
            ret = 0
            while j >= 0:
                if matrix[i][j] == 0:
                    break
                ret += 1
                j -= 1
            return ret

        m = len(matrix)
        if m == 0:
            return 0
        maxv = 0

        for i in range(m):
            sta = []
            now = matrix[i]
            now.append(0)
            j = 0
            while j < len(now):
                if len(sta) == 0 or \
                   getH(matrix, i, j) >= getH(matrix, i, sta[-1]):
                    sta.append(j)
                    j += 1
                else:
                    idx = sta.pop()
                    if len(sta) == 0:
                        width = j
                    else:
                        width = j - 1 - sta[-1]
                    maxv = max(maxv, width * getH(matrix, i, idx))
        return maxv
