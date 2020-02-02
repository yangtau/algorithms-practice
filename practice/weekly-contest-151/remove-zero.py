# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        '''
        If the accumulated sums of node `a`, `b` are the same,
        then the sum of sequence between `a` and `b` (including `b` but excluding `a`)
        is zero.
        However, zero sequences starting from `head` cannot be identify by this way.
        To make the program correct, we can add a leading zero head in the list
        '''
        zero_head = ListNode(0)
        zero_head.next = head
        sums = dict()
        node = zero_head
        acc = 0
        while node != None:
            acc += node.val
            if acc in sums:
                sums[acc].next = node.next
            else:
                sums[acc] = node
            node = node.next
        return zero_head.next
