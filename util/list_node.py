class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def get_list_from_array(arr):
    if len(arr) == 0:
        return None
    head = ListNode(-1)
    tmp = head
    for a in arr:
        head.next = ListNode(a)
        head = head.next
    return tmp.next
