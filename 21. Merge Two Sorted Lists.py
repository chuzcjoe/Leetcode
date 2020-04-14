# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        prev = head = ListNode(None)
        
        while l1 or l2:
            if not l1:
                prev.next = l2
                break
            elif not l2:
                prev.next = l1
                break
                
            elif l1.val <= l2.val:
                cur = ListNode(l1.val)
                prev.next = cur
                prev = cur
                l1 = l1.next
                
            elif l1.val > l2.val:
                cur = ListNode(l2.val)
                prev.next = cur
                prev = cur
                l2 = l2.next
        
        return head.next
    