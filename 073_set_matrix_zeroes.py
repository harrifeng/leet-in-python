"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
"""
import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        m1 = [
            [1, 2, 3],
            [4, 0, 6],
            [7, 8, 9]
        ]

        r1 = [
            [1, 0, 3],
            [0, 0, 0],
            [7, 0, 9]
        ]
        solution.setZeroes(m1)

        self.assertEqual(r1, m1)


class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        if M == 0:
            return
        N = len(matrix[0])

        rflag = []
        cflag = []

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    rflag.append(i)
                    cflag.append(j)

        for r in rflag:
            for j in range(N):
                matrix[r][j] = 0

        for i in range(M):
            for c in cflag:
                matrix[i][c] = 0
        return
