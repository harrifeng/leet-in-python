"""
Determine if a Sudoku is valid
The Sudoku board could be partially filled, where empty cells are filled with
the character '.'.
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        a1 = ["..9748...", "7........", ".2.1.9...", "..7...24.",
              ".64.1.59.", ".98...3..", "...8.3.2.", "........6", "...2759.."]
        r1 = ["519748632", "783652419", "426139875", "357986241",
              "264317598", "198524367", "975863124", "832491756", "641275983"]
        solution.solveSudoku(a1)
        self.assertEqual(r1, a1)


class Solution(object):

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in '123456789':
                        board[i] = board[i][:j] + k + board[i][j + 1:]
                        if (self.isValid(board, i, j) and
                                self.solveSudoku(board)):
                            return True
                        board[i] = board[i][:j] + '.' + board[i][j + 1:]
                    return False
        return True

    def isValid(self, board, x, y):
        for i in range(9):
            if i != x and board[i][y] == board[x][y]:
                return False
        for j in range(9):
            if j != y and board[x][j] == board[x][y]:
                return False

        a = x / 3 * 3
        b = y / 3 * 3

        for i in range(a, a + 3):
            for j in range(b, b + 3):
                if (i != x or j != y) and board[i][j] == board[x][y]:
                    return False
        return True
