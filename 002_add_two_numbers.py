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
from util.listnode import ListNode

class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertTrue(ListNode.get_list_from_array([7,0,8]),
                         solution.addTwoNumbers(ListNode.get_list_from_array([2, 4, 3]),
                                                ListNode.get_list_from_array([5, 6, 4])))
        self.assertFalse(ListNode.get_list_from_array([7, 0, 8]),
                         solution.addTwoNumbers(ListNode.get_list_from_array([1, 2, 3]),
                                                ListNode.get_list_from_array([1, 2, 3])))



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        v1 = 0
        v2 = 0
        head = ListNode(-1)
        tmp = head
        while l1 is not None or l2 is not None:
            if l1 is None:
                v1 = 0
            else:
                v1 = l1.val
            if l2 is None:
                v2 = 0
            else:
                v2 = l2.val

            sum = v1 + v2 + carry
            head.next = ListNode(sum % 10)
            carry = sum / 10

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if carry == 1:
            head.next = ListNode(1)
        return tmp.next
