"""
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.
Note:
A solution using O(n) space is pretty straight forward. Could you devise a
constant space solution?
"""

import unittest
import util.tree_node as tr
# from util.tree_node import TreeNode


class MyTest(unittest.TestCase):

    def assertTreeNodeEqual(self, t1, t2):
        if t1:
            self.assertEqual(t1.val, t2.val)
            if t1.left:
                self.assertTreeNodeEqual(t1.left, t2.left)
            if t2.left:
                self.assertTreeNodeEqual(t1.right, t2.right)

    def test(self):
        solution = Solution()
        e1 = tr.get_tree_from_array([1, '#', 2])
        r1 = tr.get_tree_from_array([2, '#', 1])
        solution.recoverTree(r1)
        self.assertTreeNodeEqual(e1, r1)


class Solution:
    # @param root, a tree node
    # @return a tree node

    def recoverTree(self, root):
        self.last = None
        self.wrongs = [None, None]
        self.recover_helper(root)
        self.wrongs[0].val, self.wrongs[
            1].val = self.wrongs[1].val, self.wrongs[0].val
        # return root

    def recover_helper(self, root):
        if not root:
            return
        self.recover_helper(root.left)
        if self.last and self.last.val > root.val:
            if not self.wrongs[0]:
                self.wrongs[0] = self.last
            self.wrongs[1] = root
        self.last = root

        self.recover_helper(root.right)
