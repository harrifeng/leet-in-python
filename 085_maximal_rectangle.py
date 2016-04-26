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
        row = len(matrix)
        col = len(matrix[0])
        h = [0 for i in range(col + 1)]
        max_area = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '0':
                    h[j] = 0
                else:
                    h[j] += 1
            max_area = max(max_area, self.largestRectangleArea(h))
        return max_area

    def largestRectangleArea(self, h):
        stack = []
        max_area = 0
        i = 0
        while i < len(h):
            if len(stack) == 0 or h[i] >= h[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                height = h[stack.pop()]
                if len(stack) == 0:
                    width = i
                else:
                    width = i - stack[-1] - 1
                max_area = max(max_area, width * height)
        return max_area
