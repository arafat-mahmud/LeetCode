class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        

        if l1.val <= l2.val:
            h = cur1 = l1
            cur2 = l2
        else:
            h = cur1 = l2
            cur2 = l1
        
        if not cur1.next:
            cur1.next = cur2
            return cur1
        
        while cur2 and cur1:
            if not cur1.next:
                cur1.next = cur2
                cur1 = None

            elif cur2.val <= cur1.next.val:

                tmp = cur1.next
                cur1.next = cur2
                cur2 = cur2.next
                cur1.next.next = tmp
            else:
                cur1 = cur1.next
        
        return h
