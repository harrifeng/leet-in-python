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
        def inorderTrav(node):
            if node is None:
                return []
            ret = []
            ret.extend(inorderTrav(node.left))
            ret.append(node.val)
            ret.extend(inorderTrav(node.right))
            return ret

        if root is None:
            return True
        line = inorderTrav(root)

        for i in range(1, len(line)):
            if line[i] <= line[i-1]:
                return False
        return True
