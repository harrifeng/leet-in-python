"""
Given a binary tree, return the postorder traversal of its nodes' values.
For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].
Note: Recursive solution is trivial, could you do it iteratively?
"""

import unittest
import util.tree_node as tr
# from util.tree_node import TreeNode


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        root = tr.get_tree_from_array([1, 2, 3])
        self.assertEqual([2, 3, 1], solution.postorderTraversal(root))

        root2 = tr.get_tree_from_array([1, '#', 2, 3])
        self.assertEqual([3, 2, 1], solution.postorderTraversal(root2))


class Solution(object):

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        ret = []
        if root.left:
            ret.extend(self.postorderTraversal(root.left))
        if root.right:
            ret.extend(self.postorderTraversal(root.right))
        ret.append(root.val)
        return ret[:]
