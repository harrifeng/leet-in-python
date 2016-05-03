"""
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's
key.
The right subtree of a node contains only nodes with keys greater than the
node's key.
Both the left and right subtrees must also be binary search trees.
"""

import unittest
import util.tree_node as tr


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertTrue(solution.isValidBST(
            tr.get_tree_from_array([1, '#', 2])))
        self.assertFalse(solution.isValidBST(tr.get_tree_from_array([1, 2])))


class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def leftV(root):
            if root is None:
                return -2 ** 32
            if root.right is None:
                return root.val
            else:
                return leftV(root.right)

        def rightV(root):
            if root is None:
                return 2 ** 32 - 1
            if root.left is None:
                return root.val
            else:
                return rightV(root.left)
        if root is None:
            return True
        return ((root.val > leftV(root.left)) and
                (root.val < rightV(root.right)) and
                self.isValidBST(root.left) and
                self.isValidBST(root.right))
