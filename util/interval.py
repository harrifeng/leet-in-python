class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def get_interval_list_from_listlist(arr):
    ret = []
    for a in arr:
        one = Interval(s=a[0], e=a[1])
        ret.append(one)
    return ret
