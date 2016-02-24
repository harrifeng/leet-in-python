class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def get_list_from_array(arr):
        if len(arr) == 0:
            return None
        head = ListNode(-1)
        tmp = head
        for a in arr:
            head.next = ListNode(a)
            head = head.next
        return tmp

    @staticmethod
    def list_equal(l1, l2):
        while l1 != None and l2 != None:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next

        if l1 == None and l2 == None:
            return True
        else:
            return False
