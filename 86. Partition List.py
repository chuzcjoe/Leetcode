# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        dummy1 = prev1 = ListNode(None)
        dummy2 = prev2 = ListNode(None)
        cur = head
        
        while cur:
            if cur.val < x:
                prev1.next = cur
                prev1 = cur
                cur = cur.next
            elif cur.val >= x:
                prev2.next = cur
                prev2 = cur
                cur = cur.next
        
        prev1.next = None
        prev2.next = None
        prev1.next = dummy2.next
        return dummy1.next