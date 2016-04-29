import Queue
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_tree_from_array(arr):
    if len(arr) == 0:
        return None
    arr.reverse()
    root = TreeNode(arr.pop())
    q = Queue.Queue(maxsize=0)
    q.put(root)

    while not q.empty():
        cur = q.get()
        if len(arr) > 0:
            cur.left = TreeNode(arr.pop())
            q.put(cur.left)
        if len(arr) > 0:
            cur.right = TreeNode(arr.pop())
            q.put(cur.right)
    return root
