"""
Given a binary tree, return the preorder traversal of its nodes' values.
For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].
Note: Recursive solution is trivial, could you do it iteratively?
"""

import unittest
import util.tree_node as tr
# from util.tree_node import TreeNode


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        root = tr.get_tree_from_array([1, 2, 3])
        self.assertEqual([1, 2, 3], solution.preorderTraversal(root))

        root2 = tr.get_tree_from_array([1, '#', 2, 3])
        self.assertEqual([1, 2, 3], solution.preorderTraversal(root2))


class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        ret = []
        ret.append(root.val)
        if root.left:
            ret.extend(self.preorderTraversal(root.left))
        if root.right:
            ret.extend(self.preorderTraversal(root.right))
        return ret[:]
