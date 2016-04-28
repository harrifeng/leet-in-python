"""
You are given two linked lists representing two non-negative numbers. The
digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.
Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
For example:
  Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
  Output: 7 -> 0 -> 8
"""

import unittest
import util.list_node as li
from util.list_node import ListNode


class MyTest(unittest.TestCase):

    def assertListNodeEqual(self, l1, l2):
        while l1 is not None and l2 is not None:
            self.assertEqual(l1.val, l2.val)
            l1 = l1.next
            l2 = l2.next
        self.assertIsNone(l1)
        self.assertIsNone(l2)

    def test(self):
        solution = Solution()
        e1 = li.get_list_from_array([1, 4, 3, 2, 5])
        a1 = li.get_list_from_array([1, 2, 3, 4, 5])
        # a1 = li.get_list_from_array([1, 2, 3, 5, 4])

        self.assertListNodeEqual(e1, solution.reverseBetween(a1, 2, 4))


class Solution(object):

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        times = n - m
        cur = dummy
        for i in range(m - 1):
            cur = cur.next
        # cur is now the first unchanged
        end = cur.next

        for i in range(times):
            tmp = cur.next
            cur.next = end.next
            end.next = end.next.next
            cur.next.next = tmp
        return dummy.next
