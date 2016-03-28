"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of
distinct solutions.
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(len([['.Q..', '...Q', 'Q...', '..Q.'],
                              ['..Q.', 'Q...', '...Q', '.Q..']]),
                         solution.totalNQueens(4))
        self.assertEqual(len([['Q....', '..Q..', '....Q', '.Q...', '...Q.'],
                              ['Q....', '...Q.', '.Q...', '....Q', '..Q..'],
                              ['.Q...', '...Q.', 'Q....', '..Q..', '....Q'],
                              ['.Q...', '....Q', '..Q..', 'Q....', '...Q.'],
                              ['..Q..', 'Q....', '...Q.', '.Q...', '....Q'],
                              ['..Q..', '....Q', '.Q...', '...Q.', 'Q....'],
                              ['...Q.', 'Q....', '..Q..', '....Q', '.Q...'],
                              ['...Q.', '.Q...', '....Q', '..Q..', 'Q....'],
                              ['....Q', '.Q...', '...Q.', 'Q....', '..Q..'],
                              ['....Q', '..Q..', 'Q....', '...Q.', '.Q...']]),
                         solution.totalNQueens(5))


class Solution(object):

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ret = []
        tmp = ['.' * n for i in range(n)]
        self.helper(n, 0, tmp, ret)
        return len(ret)

    def helper(self, n, level, tmp, ret):
        if level == n:
            ret.append(tmp[:])
            return
        for i in range(n):
            new_row = '.' * n
            tmp[level] = new_row[:i] + 'Q' + new_row[i + 1:]
            if self.is_valid(tmp, level, i):
                self.helper(n, level + 1, tmp, ret)
            tmp[level] = new_row

    def is_valid(self, board, row, col):
        for i in range(row):
            for j in range(len(board[0])):
                if board[i][j] == 'Q' and (j == col or
                                           abs(row - i) == abs(col - j)):
                    return False
        return True
