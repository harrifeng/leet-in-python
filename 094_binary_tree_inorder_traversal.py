"""
Given a binary tree, return the inorder traversal of its nodes' values.
For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].
Note: Recursive solution is trivial, could you do it iteratively?
"""

import unittest
import util.tree_node as tr
# from util.tree_node import TreeNode


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        root = tr.get_tree_from_array([1, 2, 3])
        self.assertEqual([2, 1, 3], solution.inorderTraversal(root))


class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        tmp = []
        if root.left:
            tmp.extend(self.inorderTraversal(root.left))
        tmp.append(root.val)
        if root.right:
            tmp.extend(self.inorderTraversal(root.right))
        return tmp[:]
